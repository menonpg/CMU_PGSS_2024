# Streamlit app to classify purple color starting with r, g and b inputs in text boxes and a button to make predictions, with a square image showing the color itself and the predictions side by side
import streamlit as st
import joblib
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import matplotlib

# Load the model
model = joblib.load("model.pkl")

# Add a title for this app
st.title("Purple Color Classifier using Gradient Boosting")

# Describe the app
st.write("This app uses a trained Gradient Boosting model to classify RGB values as either 'Purple' or 'Not Purple' and reports a probability score.")

# input boxes for R, G and B values
r = st.text_input("Enter the R value (0-255):")
g = st.text_input("Enter the G value (0-255):")
b = st.text_input("Enter the B value (0-255):")

# button to make predictions
if st.button("Predict"):
    # Create some test data with R, G and B columns ranging from 0 to 255
    test_data = pd.DataFrame({
        "R": [int(r)],
        "G": [int(g)],
        "B": [int(b)]
    })

    # make a prediction
    prediction = model.predict(test_data)
    prediction_proba = model.predict_proba(test_data)

    # Display the prediction
    st.write("Prediction:", prediction[0])
    st.write("Prediction probability:", round(prediction_proba[0][1], 2))

    # Display the color
    fig, ax = plt.subplots()
    ax.add_patch(patches.Rectangle((0, 0), 1, 1, color=(int(r)/255, int(g)/255, int(b)/255)))
    ax.axis("off")
    st.pyplot(fig)
    
    