# Panic-Attack-Detection-and-Adaptive-Alert-System

A real-time, AI-powered panic attack detection system designed to monitor physiological data, predict panic attacks, and provide personalized interventions. This project combines machine learning, agent-based workflows, and an intuitive user interface to offer a comprehensive solution for managing panic attacks.

---

## Features

- **Machine Learning Model**: Utilizes a Random Forest model for accurate prediction of panic attacks, trained on real-world and synthetic data.
- **Agent-Based Workflow**: Modular agents handle tasks like data preprocessing, predictions, early warnings, personalized interventions, and emergency escalation.
- **User Personalization**: Allows users to set preferences for calming interventions and emergency contacts.
- **Real-Time Feedback**: Logs user interactions to refine predictions and improve system performance.
- **Web-Based Interface**: Intuitive interface with dashboards for user management, monitoring, and agent workflows.
- **Secure Data Management**: Employs a relational database to store user data, preferences, and feedback securely.

---

## Dataset

The **WESAD dataset** (Wearable Stress and Affect Detection) was used to train the Random Forest model. This dataset consists of multimodal physiological signals collected from wearable devices, including:
- **Blood Volume Pulse (BVP)**
- **Electrodermal Activity (EDA)**
- **Heart Rate (HR)**
- **Temperature (TEMP)**
- **Accelerometer Readings (X, Y, Z)**

To augment the dataset:
1. **Synthetic Data**: Additional data was generated to simulate a diverse range of user scenarios.
2. **Labeling**: A binary label (`1` for panic attack, `0` for normal) was applied by analyzing physiological patterns indicative of stress and panic.

The final dataset, after preprocessing, included approximately 50,000 samples with balanced class distributions. The dataset was split into 80% for training and 20% for testing.

---

## Project Structure

### Backend
- **Prediction Model**: A Random Forest model trained using physiological data from the WESAD dataset and synthetic data augmentation.
- **Flask Framework**: Handles backend logic, API routes, and database interactions.
- **Database**: SQLite database for storing user profiles, preferences, feedback logs, and predictions.

### Frontend
- **HTML/CSS/JavaScript**: Provides a responsive and accessible interface for user interaction.
- **Workflow Page**: Displays the real-time status of agents in the detection process.
- **Dashboard**: Allows users to set preferences, view system status, and log feedback.

### Agents
- **Prediction Agent**: Processes input data and predicts panic attack states.
- **Early Warning Agent**: Issues alerts and provides a buffer for user acknowledgment or cancellation.
- **Personalized Alert System**: Delivers tailored interventions such as breathing exercises or calming audio.
- **Emergency Contact Agent**: Escalates alerts to emergency contacts if the user is unresponsive.
- **Feedback Agent**: Logs user feedback for refining the model and improving system sensitivity.

---

## Installation

### Prerequisites
- Python 3.7+
- Flask Framework
- SQLite Database
- Required Python Libraries: `pandas`, `scikit-learn`, `joblib`, `flask`

### Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/panic-attack-detection.git
   cd panic-attack-detection
2. Install dependencies using:
   pip install -r requirements.txt
3. Initialize the database:
   ```bash
   flask db init
   flask db migrate
   flask db upgrade
5. Run the application:
   ```bash
   flask run

Access the web application at http://127.0.0.1:5000.
