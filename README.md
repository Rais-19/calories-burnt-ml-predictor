Calories Burnt Predictor API & Web App
A modern, beginner-friendly full-stack machine learning project that predicts the number of calories burnt during exercise using an XGBoost regression model.
The project includes a FastAPI backend for predictions + a beautiful Streamlit frontend for easy user interaction.

Features:

Accurate calorie prediction using real exercise data (age, gender, height, weight, duration, heart rate, body temperature)
Clean REST API built with FastAPI (automatic interactive docs at /docs)
User-friendly web interface with Streamlit — no technical knowledge needed
Input validation (prevents wrong data)
Friendly explanations for casual users (units in cm/kg/minutes/°C)
Fun feedback (balloons, progress bar, relatable comparisons)

Project Structure
textcalories-burnt-api/
├── app.py                      # FastAPI backend (API routes)
├── requirements.txt
├── schemas/
│   └── prediction.py           # Pydantic models for input/output validation
├── services/
│   └── prediction_service.py   # Model loading & prediction logic
├── model/
│   └── calories_model.pkl      # Trained XGBoost model (pickle format)
├── frontend/
│   └── app.py                  # Streamlit web frontend
└── README.md                   # This file
How It Works

Data Collection & Model Training (done in a separate notebook)
Two CSV files: exercise.csv + calories.csv
Features: Gender, Age, Height, Weight, Duration, Heart Rate, Body Temp
Target: Calories burnt
Trained with XGBoost Regressor → saved as calories_model.pkl

Backend (FastAPI)
Loads the model once at startup
Exposes /predict endpoint
Validates input with Pydantic
Returns predicted calories

Frontend (Streamlit)
Calls the API with user input
Shows friendly form + instant result with visual feedback
