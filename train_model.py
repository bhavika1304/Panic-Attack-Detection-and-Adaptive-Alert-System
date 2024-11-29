import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
import joblib

# Load dataset
dataset_path = 'avg_dataset.csv'  # Replace with your dataset path
data = pd.read_csv(dataset_path)

# Define features (X) and target (y)
X = data.drop(columns=['Label'])  # Replace 'target' with your target column
y = data['Label']  # Replace 'target' with your target column

# Split dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the RandomForestClassifier
clf = RandomForestClassifier(random_state=42)
clf.fit(X_train, y_train)

# Evaluate the model
y_pred = clf.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"Model Accuracy: {accuracy:.2f}")
print("Classification Report:")
print(classification_report(y_test, y_pred))

# Save the trained model
model_path = 'random_forest_model.pkl'
joblib.dump(clf, model_path)
print(f"Model saved to {model_path}")
