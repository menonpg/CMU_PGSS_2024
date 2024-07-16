import gradio as gr
import joblib
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import matplotlib

# Load the model
model = joblib.load("model.pkl")

# Create some test data with R, G and B columns ranging from 0 to 255
data = np.ndarray(shape=(1, 3), dtype=np.float32)

def classify_color(r, g, b):
    # Create some test data with R, G and B columns ranging from 0 to 255
    # data[0] = [int(r), int(g), int(b)]
    test_data = pd.DataFrame({
        "R": [int(r)],
        "G": [int(g)],
        "B": [int(b)]
    })

    # make a prediction
    prediction = model.predict(data)
    prediction_proba = model.predict_proba(data)

    # Display the prediction
    prediction_text = "Purple" if prediction[0] == 1 else "Not Purple"
    prediction_proba_text = round(prediction_proba[0][1], 2)

    return prediction_text, prediction_proba_text #, fig

iface = gr.Interface(
    fn=classify_color,
    inputs=[
        gr.Number(label="R", value=0, precision=0),
        gr.Number(label="G", value=0, precision=0),
        gr.Number(label="B", value=0, precision=0)
    ],
    outputs=[
        gr.Textbox(label="Prediction"),
        gr.Textbox(label="Prediction Probability")
    ],
    title="Purple Color Classifier using Gradient Boosting",
    description="This app uses a trained Gradient Boosting model to classify RGB values as either 'Purple' or 'Not Purple' and reports a probability score."
)

iface.launch()