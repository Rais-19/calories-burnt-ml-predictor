import pickle
import pandas as pd
import numpy as np
from pathlib import Path

# pickled model path
MODEL_PATH = Path(__file__).parent.parent / "model" / "calories_model.pkl"

print(f"Looking for model at: {MODEL_PATH.absolute()}")

# Load the model once
try:
    with open(MODEL_PATH, 'rb') as file:
        model = pickle.load(file)
    print(" XGBoost model loaded successfully!")
except Exception as e:
    print(f" CRITICAL ERROR loading model: {e}")
    model = None

def predict_calories(input_data: dict) -> float:
    """
    Predict calories using the XGBoost model.
    """
    if model is None:
        raise RuntimeError("Model failed to load. Check terminal for errors.")


    print("Received input data (from API):", input_data)

    # Convert dict to DataFrame 
    df = pd.DataFrame([input_data])

    print("DataFrame columns after creation:", list(df.columns))

    # Encode gender 
    df['Gender'] = df['Gender'].map({'male': 1, 'female': 0})

    feature_order = [
        'Gender', 'Age', 'Height', 'Weight',
        'Duration', 'Heart_Rate', 'Body_Temp'
    ]




    # Reorder columns to match training order
    df = df[feature_order]

    print("Final DataFrame before prediction:\n", df)

    # Convert to numpy array
    X = df.to_numpy()

    # Make prediction
    prediction = model.predict(X)[0]

    print("Raw prediction value:", prediction)

    # Return rounded result
    return round(float(prediction), 1)