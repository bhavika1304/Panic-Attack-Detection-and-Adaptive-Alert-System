from flask import Flask, render_template, request, redirect, url_for, session, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
import mysql.connector
import joblib
import numpy as np

app = Flask(__name__)
app.secret_key = "super_secret_key"

# MySQL Configuration
db_config = {
    "host": "127.0.0.1",
    "port": 3307,
    "user": "root",
    "password": "",
    "database": "user_dashboard"
}

# MySQL Connection Function
def get_db_connection():
    try:
        return mysql.connector.connect(**db_config)
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None

# Load the trained model
try:
    model_path = 'random_forest_model.pkl'
    clf = joblib.load(model_path)
except Exception as e:
    print(f"Error loading model: {e}")
    clf = None

# Predict Route
@app.route('/predict', methods=["POST"])
def predict():
    if not clf:
        return jsonify({"error": "Model not loaded."}), 500
    try:
        input_data = request.json  # JSON payload expected
        features = np.array([input_data[key] for key in input_data.keys()]).reshape(1, -1)
        prediction = clf.predict(features)[0]  # 0: No Panic, 1: Panic
        return jsonify({"panic_detected": bool(prediction)})
    except Exception as e:
        return jsonify({"error": str(e)}), 400

# Agent Route
@app.route('/agent', methods=["GET"])
def agent():
    if "user_id" not in session:
        return redirect(url_for("login"))
    return render_template("agent.html")

# Home Page
@app.route('/')
def home():
    if "user_id" in session:
        return redirect(url_for("dashboard"))
    return render_template("login.html")

# Register Route
@app.route('/register', methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form["username"]
        email = request.form["email"]
        password = generate_password_hash(request.form["password"])
        try:
            connection = get_db_connection()
            if not connection:
                return render_template("register.html", error="Database connection failed.")
            cursor = connection.cursor()
            # Check if username or email already exists
            cursor.execute("SELECT * FROM users WHERE username = %s OR email = %s", (username, email))
            if cursor.fetchone():
                cursor.close()
                connection.close()
                return render_template("register.html", error="Username or email already exists.")
            # Insert new user
            cursor.execute("INSERT INTO users (username, email, password) VALUES (%s, %s, %s)",
                           (username, email, password))
            connection.commit()
            cursor.close()
            connection.close()
            return redirect(url_for("login"))
        except Exception as e:
            return render_template("register.html", error=f"An error occurred: {e}")
    return render_template("register.html")

# Login Route
@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        try:
            connection = get_db_connection()
            if not connection:
                return render_template("login.html", error="Database connection failed.")
            cursor = connection.cursor(dictionary=True)
            cursor.execute("SELECT * FROM users WHERE username = %s", (username,))
            user = cursor.fetchone()
            cursor.close()
            connection.close()
            if user and check_password_hash(user["password"], password):
                session["user_id"] = user["id"]
                session["username"] = user["username"]
                return redirect(url_for("dashboard"))
            return render_template("login.html", error="Invalid username or password.")
        except Exception as e:
            return render_template("login.html", error=f"An error occurred: {e}")
    return render_template("login.html")

# Dashboard Route
@app.route('/dashboard', methods=["GET", "POST"])
def dashboard():
    if "user_id" not in session or "username" not in session:
        return redirect(url_for("login"))
    user_id = session["user_id"]
    username = session["username"]
    try:
        connection = get_db_connection()
        if not connection:
            return render_template("dashboard.html", error="Database connection failed.")
        cursor = connection.cursor(dictionary=True)
        # Fetch preferences
        cursor.execute("SELECT * FROM preferences WHERE user_id = %s", (user_id,))
        preferences = cursor.fetchone()
        # Update preferences if POST
        if request.method == "POST":
            relaxation_method = request.form["relaxation_method"]
            emergency_contact = request.form["emergency_contact"]
            cursor.execute(
                "REPLACE INTO preferences (user_id, relaxation_method, emergency_contact) VALUES (%s, %s, %s)",
                (user_id, relaxation_method, emergency_contact)
            )
            connection.commit()
        cursor.close()
        connection.close()
        return render_template("dashboard.html", preferences=preferences, username=username)
    except Exception as e:
        return render_template("dashboard.html", error=f"An error occurred: {e}")

# Logout Route
@app.route('/logout')
def logout():
    session.pop("user_id", None)
    session.pop("username", None)
    return redirect(url_for("home"))

if __name__ == "__main__":
    app.run(debug=True)
