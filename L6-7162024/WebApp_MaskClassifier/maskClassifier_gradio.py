import gradio as gr
from keras.models import load_model  # TensorFlow is required for Keras to work
from PIL import Image, ImageOps  # Install pillow instead of PIL
import numpy as np
import os

# Disable scientific notation for clarity
np.set_printoptions(suppress=True)

# Load the model
model = load_model("../../L5-7122024/MaskClassifier/keras_Model.h5", compile=False)

# Load the labels
class_names = open("../../L5-7122024/MaskClassifier/labels.txt", "r").readlines()

# Create the array of the right shape to feed into the keras model
data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

def classify_image(image):
    image = ImageOps.fit(image, (224, 224), Image.Resampling.LANCZOS)
    
    # Turn the image into a numpy array
    image_array = np.asarray(image)

    # Normalize the image
    normalized_image_array = (image_array.astype(np.float32) / 127.5) - 1

    # Load the image into the array
    data[0] = normalized_image_array

    # Predicts the model
    prediction = model.predict(data)
    index = np.argmax(prediction)
    class_name = class_names[index]
    confidence_score = prediction[0][index]

    return f"Class: {class_name[2:]}", f"Confidence Score: {confidence_score}"

# Create the Gradio interface
iface = gr.Interface(
    fn=classify_image,
    inputs=gr.inputs.Image(type="pil"),
    outputs=[
        gr.outputs.Textbox(label="Prediction"),
        gr.outputs.Textbox(label="Confidence Score")
    ],
    title="Image based Mask Classifier",
    description="This app uses a trained Keras model built using Google's Teachable Machine to classify images as either 'Mask' or 'No Mask' and reports a confidence score."
)

# Launch the app
iface.launch()
