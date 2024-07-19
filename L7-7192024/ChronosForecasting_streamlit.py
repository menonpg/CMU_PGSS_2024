import pandas as pd
import torch
import os
from chronos import ChronosPipeline
# pip install git+https://github.com/amazon-science/chronos-forecasting.git
import streamlit as st
from datetime import datetime
import glob
import plotly.express as px
import numpy as np
import plotly.graph_objects as go

# Load the Chronos model
pipeline = ChronosPipeline.from_pretrained(
    "amazon/chronos-t5-small",
    device_map="cuda",  # use "cpu" for CPU inference and "mps" for Apple Silicon
    torch_dtype=torch.bfloat16,
)

# Create a file uploader widget
uploaded_file = st.sidebar.file_uploader("Upload your CSV file", type="csv")

if uploaded_file is None:
    # If no file is uploaded, provide a selectbox of available files
    # List all files ending with .csv in the current directory
    csv_files = glob.glob("./*.csv")
    selected_file = st.sidebar.selectbox("Select a CSV file", csv_files)

# Load the time series data from the CSV file
# @st.cache_resource
def load_data():
    if uploaded_file is not None:
        # Read the uploaded CSV file
        df = pd.read_csv(uploaded_file)

    else:

        if selected_file:
            df = pd.read_csv(selected_file)

    return df

df = load_data()

# Convert the 'time' column to datetime format
df['time'] = pd.to_datetime(df['time'])

# Set the 'value' column as the target variable for forecasting
target_col = "value"

# Create a Streamlit app
st.title("Time Series Forecasting with Chronos")

st.sidebar.header("Data")
st.sidebar.write(df.head())

st.header("Forecast")
forecast_col = st.selectbox(
    "Select the column to forecast",
    ["value"],
)

# Ensure the 'time' column is in datetime format
df['time'] = pd.to_datetime(df['time'])

# Find the maximum date in the 'time' column
max_date = df['time'].max()

# Use the maximum date as the start date in your Streamlit sidebar
start_date = st.sidebar.date_input("Start date for forecasting", value=max_date)

# Set the end date to 10 days after the start date
prediction_length = st.sidebar.slider("Prediction duration:",5,30, 10, 1)
end_date = st.sidebar.date_input("End date for forecasting", value=max_date + pd.Timedelta(days=prediction_length))

# Use the Chronos model to forecast the time series
@st.cache_resource
def make_forecast(start_date, end_date):
    context = torch.tensor(df[target_col].values)
    prediction_length = (end_date - start_date).days

    # Create a forecast for the selected time range
    forecast = pipeline.predict(
        context,
        prediction_length,
        num_samples=20,
        temperature=1.0,
        top_k=50,
        top_p=1.0,
    )

    return forecast

forecast_start_date = start_date.strftime("%Y-%m-%d")
forecast_end_date = end_date.strftime("%Y-%m-%d")

forecast = make_forecast(start_date, end_date)

with st.expander("Forecasted Values", expanded=False):
    st.write(forecast)

# visualize the forecast
forecast_index = list(range(len(df), len(df) + prediction_length))
low, median, high = np.quantile(forecast[0].numpy(), [0.1, 0.5, 0.9], axis=0)

# Create a figure
fig = go.Figure()

# Add historical data to the plot
fig.add_trace(go.Scatter(x=df.index, y=df["value"],
                         mode='lines',
                         name='historical data',
                         line=dict(color='royalblue')))

# Add median forecast
fig.add_trace(go.Scatter(x=forecast_index, y=median,
                         mode='lines',
                         name='median forecast',
                         line=dict(color='tomato')))

# Add 80% prediction interval
fig.add_trace(go.Scatter(x=forecast_index, y=low,
                         mode='lines',
                         name='80% prediction interval lower',
                         showlegend=False,
                         line=dict(width=0)))
fig.add_trace(go.Scatter(x=forecast_index, y=high,
                         mode='lines',
                         name='80% prediction interval upper',
                         fill='tonexty',  # fill area between trace0 and trace1
                         fillcolor='tomato', opacity=0.3,
                         line=dict(width=0)))

# Update layout options
fig.update_layout(title='Historical Data and Median Forecast with 80% Prediction Interval',
                  xaxis_title='Index',
                  yaxis_title='Value',
                  legend_title='Legend',
                  template='plotly_white')

st.plotly_chart(fig)