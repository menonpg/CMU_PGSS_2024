# CMU PGSS 2024 Course Repository
Coursework repository for PGSS 2024, at Carnegie Mellon University.

# Week 1 Lecture Notes
*L1 and L2: Introduction to R and Python, IDEs and Local Development Evironments equipped with GenAI (Github Copilot, Ollama models)*

## Setup for Development Environment

### 1. Development Environment
- **Local:**
  - Setting up a local development environment on your personal machine.
  - Commonly used IDEs (Integrated Development Environments) and tools.

- **Cloud:**
  - Utilizing cloud-based development environments for flexibility and collaboration.
  - Examples include:
    - **Google Colab:** A cloud-based notebook environment that supports Python.
    - **Lightning.ai:** A platform for building and deploying AI models.
    - **Posit.cloud:** A cloud-based environment for R and Python.

### 2. Languages
- **R:** 
  - Commonly used for statistical computing and graphics.
  - Useful in data analysis and machine learning tasks.
- **Python:**
  - Versatile programming language with extensive libraries for data science, machine learning, and AI.
- **Markdown:**
  - A lightweight markup language for creating formatted text using a plain-text editor.
  - Useful for writing documentation, README files, and notes.

### 3. Code Versioning
- **Git:**
  - A distributed version control system for tracking changes in source code.
  - Essential for collaboration and managing code versions.
- **GitHub:**
  - A platform for hosting and collaborating on Git repositories.
  - Provides version control and project management tools.

### 4. GenAI (Generative AI)
- **Github Copilot:**
  - An AI-powered code completion tool that suggests code snippets based on the context.
- **Local Language Models (LLMs):**
  - Utilizing local instances of language models for various AI tasks.
  - Examples include Ollama, which can be integrated into development workflows.
 
 
---
---

# Week 2 Lecture Notes

*L3 - 7/2/2024: Working with Tabular Data [Regression vs Classification]*

---

#### Datasets to Explore:

1. **UC Irvine ML Datasets Repository:**
   - [UCI ML Repository](https://archive.ics.uci.edu/datasets)

2. **Internal Datasets:**
   - **R:**
     ```R
     library(datasets)
     ```
   - **Sklearn Datasets:**
     ```python
     from sklearn.datasets import load_iris
     iris = load_iris()
     ```

---

#### Key Topics:

1. **Building Classification and Regression Models from Tabular Data:**
   - Understand the difference between classification (categorizing data) and regression (predicting continuous values).

2. **Understanding Boxplots:**
   - Learn how to use boxplots to separate categorical classes based on a continuous variable.

3. **Statistical Tests:**
   - Introduction to statistical tests with a focus on the t-test, which compares the means of two groups.

4. **Classification:**
   - Definition and examples of classification problems.
   - Techniques for building classification models.

5. **Regression:**
   - Definition and examples of regression problems.
   - Techniques for building regression models.

6. **Building a Classification Model in R and Python (Logistic Regression):**
   - Steps to create logistic regression models in both R and Python.

7. **Building a Regression Model in R:**
   - Steps to create regression models in R.

8. **Using Notebooks in R and Publishing to RPubs:**
   - How to create and publish R Notebooks to RPubs for public viewing.

9. **Opening .ipynb Files in GitHub Using Colab:**
   - Use the Colab plugin or a custom Readme-specific line of code to open Jupyter notebooks (.ipynb) in GitHub.

10. **Building a StreamLit App:**
    - Steps to create a StreamLit app to host a model for web-based interactive inference.

---

#### Tensorflow Playground:

- **Interactive Learning Tool:**
  - [Tensorflow Playground](https://playground.tensorflow.org/#activation=tanh&batchSize=10&dataset=circle&regDataset=reg-plane&learningRate=0.03&regularizationRate=0&noise=0&networkShape=4,2&seed=0.86874&showTestData=false&discretize=false&percTrainData=50&x=true&y=true&xTimesY=false&xSquared=false&ySquared=false&cosX=false&sinX=false&cosY=false&sinY=false&collectStats=false&problem=classification&initZero=false&hideText=false)

---

---

# Week 3 Lecture Notes

### Working with AutoML Tools, Understanding Classification Models and Metrics for Performance in Binary and Multi-Class Classification and Regression + Images and WebCam Feeds [Building Portable AI from a Teachable Machine]

#### Lecture 4: Deploying an ML Model in Production - Show and Tell

**Topics Covered:**
1. **Tabular Data Driven Model**
   - Understanding the structure and importance of tabular data in machine learning.
   - How to preprocess and clean tabular data for model training.

2. **H2o.AI**
   - Introduction to H2o.AI and its functionalities.
   - Demonstration of using H2o.AI for building machine learning models.
   - Advantages of using H2o.AI for AutoML.

3. **AutoML Tools**
   - Overview of various AutoML tools available in the market.
   - Comparison of different AutoML tools based on features and performance.
   - Practical session on using AutoML tools to automate the machine learning pipeline.

4. **Ensemble Models**
   - Explanation of ensemble learning and its types (Bagging, Boosting, Stacking).
   - How ensemble models improve the performance of machine learning models.
   - Implementation of ensemble models using popular libraries.

5. **Linear vs Non-linear Model Types**
   - Differences between linear and non-linear models.
   - Examples of linear models (e.g., Linear Regression, Logistic Regression).
   - Examples of non-linear models (e.g., Decision Trees, Neural Networks).

6. **Typical Model Performance Metrics**
   - Key performance metrics for evaluating machine learning models.
   - Metrics for regression models (e.g., MSE, RMSE, MAE).
   - Metrics for classification models (e.g., Accuracy, Precision, Recall, F1 Score).

7. **Image Models and AutoML**
   - Introduction to image models and their applications.
   - Using AutoML tools for building and deploying image classification models.
   - Case study on deploying an image model using AutoML.

---

#### Lecture 5:

**Topics Covered:**

1. **Crowd-sourcing Data**
   - Importance of crowd-sourced data in machine learning.
   - How to collect and use crowd-sourced data for model training.
   - Resources:
     - [RGB Color Chart](https://www.rapidtables.com/web/color/RGB_Color.html)
     - [Google Spreadsheet for Data Collection](https://docs.google.com/spreadsheets/d/1e4tKP4QaNnCz8yqSYSBWG6fO6wfFhwJI3xzfp4XD8Lo/edit?usp=sharing)

2. **Linear vs Non-linear Models**
   - In-depth discussion on linear and non-linear models.
   - Scenarios where linear models are preferred over non-linear models and vice versa.
   - Practical examples and case studies.

3. **Technical Review of Classification Metrics**
   - Detailed analysis of classification metrics.
   - Understanding the confusion matrix and its components.
   - Advanced metrics for multi-class classification problems.

4. **Teachable Machine**
   - Introduction to Google's Teachable Machine.
   - How to use Teachable Machine for creating and training image models.
   - Practical session on building a portable AI using Teachable Machine.
   - Resource for data collection: [Google Drive Folder for Modeling Images](https://drive.google.com/drive/folders/1TpveL7qAaT0q-BB7375OTbX0e-_lW-QY?usp=drive_link)

---

### Summary:
This week focuses on understanding and working with AutoML tools, deploying machine learning models in production, and evaluating model performance using various metrics. Additionally, the lectures cover the differences between linear and non-linear models, the importance of crowd-sourced data, and practical sessions on using Teachable Machine for building portable AI models.


---

---
# Week 4 Lecture Notes

## Developing and Hosting and Deployment of Web Applications that Expose Pre-trained Machine Learning Models

### Streamlit
- Streamlit is an open-source app framework for Machine Learning and Data Science teams.
- It allows you to create and share custom web apps for machine learning and data science.
- It’s easy to use, requiring only a few lines of Python code to create interactive web applications.

### Gradio
- Gradio is a Python library that allows you to quickly create customizable UI components around your machine learning models.
- It provides an easy way to demo your models using a web interface.

### Huggingface Spaces
- Huggingface Spaces is a hosted service that allows you to deploy machine learning models and applications.
- It supports various frameworks including Streamlit and Gradio, making it easy to host and share your applications.

### Streamlit Hub
- Streamlit Hub is a platform for hosting and sharing Streamlit applications.
- It allows you to deploy your Streamlit apps with ease and collaborate with others.

## How to Use the Mask Classifier Streamlit App

To run the Mask Classifier Streamlit app, use the following command:
```python
streamlit run maskClassifier_streamlit.py
```
The app opens on port 8501 by default, on the localhost.

## How to Use the Mask Classifier Gradio App

To run the Mask Classifier Gradio app, use the following command:
```python
python maskClassifier_gradio.py
```
The app opens on port 7860 by default, on the localhost.

## How to Use the Purple Classifier Streamlit App

To run the Purple Classifier Streamlit app, use the following command:
```python
streamlit run PurpleClassifier_streamlit.py
```
The app opens on port 8501 by default, on the localhost.

## How to Use the Purple Classifier Gradio App

To run the Purple Classifier Gradio app, use the following command:
```python
python PurpleClassifier_gradio.py
```
The app opens on port 7860 by default, on the localhost.

## Next Class: Exposure to Time Series Data and Forecasting

- Time series data and examples
- Time series forecasting using typical models (Holt Winters model, Linear Forecasting)
- Time series forecasting using deep learning transformer models: Amazon Chronos
