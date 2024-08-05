import sys
import os
import joblib
import pandas as pd
from spamemail import logging
from spamemail import CustomException
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from imblearn.over_sampling import SMOTE
from spamemail.entity import DataTransformationConfig
 

class DataTransformation:
    def __init__(self, config: DataTransformationConfig):
        self.config = config

    
    ## Note: You can add different data transformation techniques such as Scaler, PCA and all
    # You can perform all kinds of EDA in ML cycle here before passing this data to the model

    # Only the train_test_spliting is done here since this data is already cleaned up

    def Data_transformation(self):
        try: 
            df = pd.read_csv(self.config.data_path)
            logging.info('Reading Data...')
            logging.info('Vectorization initiated')

            # Vectorization using CountVectorizer
            cv = CountVectorizer()
            x = df['Message']
            y = df['Category'].apply(lambda x: 1 if x == 'spam' else 0)  # Convert labels to binary values
            x_vectorized = cv.fit_transform(x)
            logging.info('Vectorization Completed')


            # Save CountVectorizer to a file
            vectorizer_path = os.path.join(self.config.root_dir, 'count_vectorizer.pkl')
            joblib.dump(cv, vectorizer_path)

            # SMOTE oversampling
            smote = SMOTE(random_state=42)
            x_resampled, y_resampled = smote.fit_resample(x_vectorized, y)
            logging.info('Oversampling Completed')

            # Splitting Dataset into training and testing sets
            x_train, x_test, y_train, y_test = train_test_split(x_resampled, y_resampled, test_size=0.2, random_state=42)
            logging.info('Data Splitting is Completed')
            return x_train, x_test, y_train, y_test
        
        except Exception as e:
            raise CustomException(f"An error occurred during data transformation: {str(e)}", sys)