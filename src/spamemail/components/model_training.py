import sys
import os
import joblib
import pandas as pd
from spamemail import logging
from spamemail import CustomException
from spamemail.constants import TIMESTAMP

import matplotlib.pyplot as plt
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from tensorflow.keras.callbacks import EarlyStopping
from tensorflow.keras.models import save_model
 
 
class ModelTrainer:
    def __init__(self, config):
        self.config = config

    def train_model(self, x_train, x_test, y_train, y_test):
        logging.info('Building Model')

        # Build the Deep Learning Model
        model = Sequential()
        model.add(Dense(64, activation='relu', input_dim=x_train.shape[1]))
        model.add(Dropout(0.7))
        model.add(Dense(32, activation='relu'))
        model.add(Dense(1, activation='sigmoid'))

        # Compile the model
        model.compile(optimizer=self.config.optimizer, loss=self.config.loss, metrics=self.config.metrics)
        model.summary()
        logging.info('Model Built')

        # Early stopping to prevent overfitting
        early_stopping = EarlyStopping(monitor='val_loss', patience=3, restore_best_weights=True)

        # Train the model
        history = model.fit(x_train, y_train, epochs=10, batch_size=32, validation_data=(x_test, y_test), callbacks=[early_stopping], verbose=1)
        logging.info('Model Trained')
        
        # Save the trained model
        model.save(os.path.join(self.config.root_dir, self.config.model_name))

        logging.info(' Model Saved')
        # Evaluate the model
        y_pred_prob = model.predict(x_test)
        y_pred = (y_pred_prob > 0.5).astype(int)

        accuracy = accuracy_score(y_test, y_pred)
        precision = precision_score(y_test, y_pred, pos_label=1)
        recall = recall_score(y_test, y_pred, pos_label=1)
        f1 = f1_score(y_test, y_pred, pos_label=1)

        print(f'Accuracy: {accuracy:.4f}')
        print(f'Precision: {precision:.4f}')
        print(f'Recall: {recall:.4f}')
        print(f'F1 score: {f1:.4f}')

        # Visualize training history
        plt.figure(figsize=(10, 6))

        # Plot training & validation accuracy values
        plt.subplot(1, 2, 1)
        plt.plot(history.history['accuracy'])
        plt.plot(history.history['val_accuracy'])
        plt.title('Model accuracy')
        plt.ylabel('Accuracy')
        plt.xlabel('Epoch')
        plt.legend(['Train', 'Validation'], loc='upper left')

        # Plot training & validation loss values
        plt.subplot(1, 2, 2)
        plt.plot(history.history['loss'])
        plt.plot(history.history['val_loss'])
        plt.title('Model loss')
        plt.ylabel('Loss')
        plt.xlabel('Epoch')
        plt.legend(['Train', 'Validation'], loc='upper left')

        plt.tight_layout()
        #plt.show()
        
        # Save plot with a timestamp
        filename = f"{self.config.model_figure_path}_accuracy_loss_{TIMESTAMP}.png"
        logging.info(f"Save model accuracy loss to {filename}")
        plt.savefig(filename)
        plt.close()
        logging.info(f'Model accuracy and loss saved as {filename}')