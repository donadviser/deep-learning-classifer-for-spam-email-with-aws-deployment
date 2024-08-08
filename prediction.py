import joblib
from pathlib import Path
import tensorflow as tf

# Save the CountVectorizer to disk
vectorizer_filename = Path('artefacts/data_transformation/count_vectorizer.pkl')

# Save the trained model to disk
model_filename = Path('artefacts/model_trainer/model.h5')

# Load the CountVectorizer from disk
loaded_vectorizer = joblib.load(vectorizer_filename)

# Load the trained model from disk
loaded_model = tf.keras.models.load_model(model_filename)

# Example usage: Vectorize new data and make predictions
new_emails = ["Todays Voda numbers ending 7548 are selected to receive a $350 award. If you have a match please call", "Congratulations! You've won a free ticket to the Bahamas!", "Please find the attached report for this quarter.","Nah I don't think he goes to usf, he lives around here though"]
new_emails_vectorized = loaded_vectorizer.transform(new_emails)

# Predict using the loaded model
predictions = loaded_model.predict(new_emails_vectorized)
print(predictions)
predicted_classes = (predictions > 0.9).astype(int)

for email, prediction in zip(new_emails, predicted_classes):
    print(f"Email: {email}\nPrediction: {'Spam' if prediction else 'Ham'}\n")