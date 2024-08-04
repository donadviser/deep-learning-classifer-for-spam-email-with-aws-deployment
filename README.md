# Deep Learning for Spam Email Classification Deployed on AWS

This project implements a Neural Network Classifier for Spam Classification, achieving great accuracy (~97%) and deployed on AWS. It covers the complete lifecycle of an ML project from data collection to deployment.

## Project Overview

This project focuses on building and deploying a machine learning model for spam email classification using a Neural Network. Key phases of the project include:

- **Data Collection:** Utilized a dataset of spam and non-spam emails for training the classifier.
- **Data Preprocessing:** Cleaned and prepared the dataset for model training.
- **Model Training:** Developed a Neural Network model using TensorFlow/Keras to classify emails.
- **Model Evaluation:** Evaluated the model's performance using metrics like accuracy, precision, recall, and F1-score.
- **Model Deployment:** Deployed the trained model on AWS using Streamlit for interactive web application deployment.

## Motivation
The motivation behind this project is to demonstrate the end-to-end process of deploying a machine learning model, emphasizing the importance of deployment skills for aspiring Data Scientists and ML engineers.

## Workflows

The workflow begins with creating a virtual environment, `template.py`, `setup.py`, and `requirements.txt` to establish the file and directory structure and create a package. The remainder of the workflow follows a loop of the steps below:

1. Update `config.yaml`
2. Update `secrets.yaml` [Optional]
3. Update `params.yaml`
4. Update the entity
5. Update the configuration manager in `src/config`
6. Update the components
7. Update the pipeline
8. Update `main.py`
9. Update `dvc.yaml`


## Tech Stacks
 - **Python:** Programming language used for data preprocessing, model training, and deployment.
 - **TensorFlow/Keras:** Deep learning framework used to build and train the Neural Network model.
 - **Streamlit:** Used for building and deploying the web application for model inference.
 - **AWS (Amazon Web Services):** Cloud platform used for model deployment.
 - **Joblib:** Library used for saving and loading models.
 - **Scikit-learn:** Used for various machine learning utilities including metrics calculation and data preprocessing.
 - **NLTK and WordCloud:** Used for natural language processing and visualization tasks.
 
 ## Let's Connect
 For any issues or questions related to this project, feel free to reach out through the following channels:
 
 - **X:** [twitter](https://x.com/donadviser) 
 - **LinkedIn:** [LinkedIn Profile](https://www.linkedin.com/in/donadviser/) 👔
 - **Medium:** [Medium Blog](https://medium.com/@donadviser) ✍️
 
 Your feedback and contributions are greatly appreciated!
 
*By Derrick Njobuenwu, PhD*