# Panic-Attack-Detection-and-Adaptive-Alert-System

A real-time, AI-powered panic attack detection system designed to monitor physiological data, predict panic attacks, and provide personalized interventions. This project combines machine learning, agent-based workflows, and an intuitive user interface to offer a comprehensive solution for managing panic attacks.

---

## Features

- **Machine Learning Model**: Utilizes a Random Forest model for accurate prediction of panic attacks.
- **Agent-Based Workflow**: Modular agents handle tasks like data preprocessing, predictions, early warnings, personalized interventions, and emergency escalation.
- **User Personalization**: Allows users to set preferences for calming interventions and emergency contacts.
- **Real-Time Feedback**: Logs user interactions to refine predictions and system performance.
- **Web-Based Interface**: User-friendly interface with dashboards for monitoring and setting preferences.

---

## Project Structure

### Backend
- **Prediction Model**: Machine learning model trained on the WESAD dataset with synthetic data augmentation.
- **Flask Framework**: Handles backend logic and API routes.
- **Database**: SQLite database for managing user data, preferences, feedback, and predictions.

### Frontend
- **HTML/CSS/JavaScript**: Clean, responsive user interface for registration, login, dashboard, and real-time monitoring.
- **Workflow Page**: Displays the status of all agents in the detection workflow.

### Agents
- **Prediction Agent**: Analyzes physiological data to detect potential panic attacks.
- **Early Warning Agent**: Issues alerts with a buffer period for user response.
- **Personalized Alert System**: Provides calming interventions based on user preferences.
- **Emergency Contact Agent**: Notifies emergency contacts if the user is unresponsive.
- **Feedback Agent**: Logs user responses for system refinement.

---

## Installation

### Prerequisites
- Python 3.7+
- Flask
- SQLite
- Required Python libraries: `pandas`, `scikit-learn`, `joblib`, `flask`

### Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/panic-attack-detection.git
   cd panic-attack-detection
2. Install dependencies using:
   pip install -r requirements.txt
3. Initialize the database:
   flask db init
   flask db migrate
   flask db upgrade
4. Run the application:
   flask run

Access the web application at http://127.0.0.1:5000.
