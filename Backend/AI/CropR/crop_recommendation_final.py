# -*- coding: utf-8 -*-
"""crop_recommendation_final.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1cmUZtXODeoXiXck3kJ9SHUQc1cRCCgKO
"""

import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, r2_score
import pickle

# Load the dataset
crop_recommendation_df = pd.read_csv('/content/Crop_recommendation.csv')

# Display the first few rows and unique labels
print(crop_recommendation_df.head())
print(crop_recommendation_df['label'].unique())

# Split features and target
features = crop_recommendation_df[crop_recommendation_df.columns.drop("label")]
target = crop_recommendation_df["label"]

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(features, target, test_size=0.1, random_state=42)

# Initialize and train the model
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Make predictions and check the score
predictions = model.predict(X_test)
print(f"Accuracy Score: {accuracy_score(y_test, predictions):.2f}")

# Save the model
with open('crop_recommendation_model.pkl', 'wb') as file:
    pickle.dump(model, file)

print("Model saved successfully.")

# To demonstrate loading and using the saved model
# Load the saved model
with open('crop_recommendation_model.pkl', 'rb') as file:
    loaded_model = pickle.load(file)

# Use the loaded model to make predictions
loaded_predictions = loaded_model.predict(X_test)
print(f"Accuracy Score (using loaded model): {accuracy_score(y_test, loaded_predictions):.2f}")

# Example of using the model for a single prediction
# Replace these with actual values from user input in your application
sample_input = np.array([[90, 42, 43, 20.879744, 82.002744, 6.502985, 202.935536]])

# Make sure the feature names match those used during training
feature_names = ['N', 'P', 'K', 'temperature', 'humidity', 'ph', 'rainfall']
sample_df = pd.DataFrame(sample_input, columns=feature_names)

# Make prediction
sample_prediction = loaded_model.predict(sample_df)
print(f"Recommended crop for the sample input: {sample_prediction[0]}")