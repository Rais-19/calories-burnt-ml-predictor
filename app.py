from fastapi import FastAPI
from schemas.prediction import PredictionInput, PredictionOutput   
from services.prediction_service import predict_calories          
from typing import Literal


app = FastAPI(
    title="Calories Burnt Prediction API",
    description="Simple API to predict calories burnt during exercise using XGBoost",
    version="1.0.0"
)

# --- Endpoints ---

@app.get("/")
def read_root():
    return {"message": "Welcome to the Calories Burnt Prediction API!"}

@app.get("/health")
def health_check():
    return {"status": "healthy"}

@app.post("/predict", response_model=PredictionOutput)
def predict(input_data: PredictionInput):
    """
    Predict calories burnt based on exercise features.
    """
    # Call the prediction service (we'll implement this next)
    prediction = predict_calories(input_data.dict())
    
    return {"predicted_calories": prediction}