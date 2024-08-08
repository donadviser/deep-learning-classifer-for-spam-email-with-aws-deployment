import sys
import json
from spamemail import logging
from spamemail import CustomException
from spamemail.constants import TIMESTAMP
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import (
    accuracy_score, 
    precision_score, 
    recall_score, 
    f1_score, 
    confusion_matrix,
    roc_auc_score, 
    roc_curve,
    )
from tensorflow.keras.models import load_model
import tensorflow as tf


class ModelEvaluation:
    def __init__(self, config):
        self.config = config
    
    def eval(self, x_test, y_test):
        try:
            # Load the model from the specified path
            logging.info('Model Loading')
            model = load_model(self.config.model_path)
            logging.info('Model Loaded')        
            # Evaluate the model

            # Check if x_test is a SciPy sparse matrix
            if hasattr(x_test, 'tocoo'):
                logging.info('Converting SciPy sparse matrix to TensorFlow SparseTensor')
                x_test_coo = x_test.tocoo()  # Convert to COO format if not already
                indices = np.vstack((x_test_coo.row, x_test_coo.col)).T
                values = x_test_coo.data
                shape = x_test_coo.shape
                x_test_sparse = tf.sparse.SparseTensor(indices, values, shape)
                x_test_sparse = tf.sparse.reorder(x_test_sparse)
            else:
                # Convert to dense tensor if already dense
                logging.info('Using dense format for x_test')
                x_test_sparse = tf.convert_to_tensor(x_test)

            # Use x_test_sparse in model prediction
            y_pred_prob = model.predict(x_test_sparse)

            logging.info('Prediction is completed')
            y_pred = (y_pred_prob > 0.5).astype(int)

            # Calculate metrics
            metrics = {
                'accuracy': accuracy_score(y_test, y_pred),
                'precision': precision_score(y_test, y_pred),
                'recall': recall_score(y_test, y_pred),
                'f1_score': f1_score(y_test, y_pred),
                'roc_auc': roc_auc_score(y_test, y_pred_prob),
            }
            
            # Confusion Matrix
            conf_matrix = confusion_matrix(y_test, y_pred)
            metrics['confusion_matrix'] = conf_matrix.tolist()
            
            # Plotting Confusion Matrix
            plt.figure(figsize=(8, 6))
            sns.heatmap(conf_matrix, annot=True, cmap="coolwarm", fmt="d")
            plt.xlabel('Predicted label')
            plt.ylabel('True label')
            plt.title('Confusion Matrix')
            conf_matrix_filename = f"{self.config.metric_figure_path}_confusion_matrix_{TIMESTAMP}.png"
            logging.info(f"Save Confusion matrix to {conf_matrix_filename}")
            plt.savefig(conf_matrix_filename)
            plt.close()
            logging.info(f'Confusion matrix saved as {conf_matrix_filename}')

            # ROC Curve
            fpr, tpr, _ = roc_curve(y_test, y_pred_prob)
            plt.figure(figsize=(8, 6))
            plt.plot(fpr, tpr, marker='.')
            plt.title('Receiver Operating Characteristic (ROC) Curve')
            plt.xlabel('False Positive Rate')
            plt.ylabel('True Positive Rate')
            plt.grid(True)
            roc_curve_filename = f"{self.config.metric_figure_path}_roc_curve_{TIMESTAMP}.png"
            plt.savefig(roc_curve_filename)
            logging.info(f'ROC curve saved as {roc_curve_filename}')
            plt.close()

            # Save metrics to a JSON file
            metrics_filename = f"{self.config.metrics_json_file}"
            with open(metrics_filename, 'w') as f:
                json.dump(metrics, f, indent=4)
            logging.info(f'Metrics saved as {metrics_filename}')

        except Exception as e:
            raise CustomException(f"An error occurred while evaluating the model: {e}", sys)