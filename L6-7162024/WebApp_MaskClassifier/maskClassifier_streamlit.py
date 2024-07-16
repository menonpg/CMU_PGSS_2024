# Design the streamlit app.  The app will have a title, a file uploader for an image, and a button to make predictions and display the result. 

import streamlit as st
from keras.models import load_model  # TensorFlow is required for Keras to work
from PIL import Image, ImageOps  # Install pillow instead of PIL
import numpy as np
import os

# Disable scientific notation for clarity
np.set_printoptions(suppress=True)

# Add a title for this app
st.title("Image based Mask Classifier")

# Describe the app
st.write("This app uses a trained Keras model built using Google's Teachable Machine to classify images as either 'Mask' or 'No Mask' and reports a confidence score.")

# Load the model
model = load_model("../../L5-7122024/MaskClassifier/keras_Model.h5", compile=False)

# Load the labels
class_names = open("../../L5-7122024/MaskClassifier/labels.txt", "r").readlines()

# Create the array of the right shape to feed into the keras model
# The 'length' or number of images you can put into the array is
# determined by the first position in the shape tuple, in this case 1
data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

# Load the image from the upload file dialog
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

# Save the file as an image in an uploads folder - create it if it does't exist
# Check if the "uploads/" directory exists and if not create it
if not os.path.exists("uploads"):
    os.makedirs("uploads")
    
if uploaded_file is not None:
    with open("uploads/" + uploaded_file.name, "wb") as f:
        f.write(uploaded_file.getbuffer())
        # st.write("Saved file:", uploaded_file.name)

def classify_image(uploaded_file):
    
        image = Image.open(uploaded_file).convert("RGB")

        # resizing the image to be at least 224x224 and then cropping from the center
        size = (224, 224)
        image = ImageOps.fit(image, size, Image.Resampling.LANCZOS)

        # turn the image into a numpy array
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

        # Print prediction and confidence score
        if class_name[2:] == "Mask":
            st.success("Class: " + class_name[2:])
        else:
            st.error("Class: " + class_name[2:])
        
        st.write("Confidence Score: ", confidence_score)

if uploaded_file is not None:
    
    if st.button("Submit"):
        classify_image(uploaded_file)
    
else:
    # Select a file from the uploads/ folder 
    uploaded_files = os.listdir("uploads")
    if len(uploaded_files) > 0:
        selected_file = st.sidebar.selectbox("Select a file from the uploads folder", uploaded_files)
        image = Image.open("uploads/" + selected_file)
        st.image(image, caption="Uploaded Image", use_column_width=True)
    else:
        st.write("Please upload an image file.")
          
    classify_image("uploads/" + selected_file)
        
    