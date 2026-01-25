from pydantic import BaseModel, Field
from typing import Literal

class PredictionInput(BaseModel):
    Gender: Literal["male", "female"] = Field(..., description="Gender of the person (must be 'male' or 'female')")
    Age: int = Field(..., gt=0, le=100, description="Age in years (1-100)")
    Height: float = Field(..., gt=100, le=250, description="Height in cm (100-250)")
    Weight: float = Field(..., gt=30, le=200, description="Weight in kg (30-200)")
    Duration: float = Field(..., gt=0, le=300, description="Exercise duration in minutes (0-300)")
    Heart_Rate: float = Field(..., gt=50, le=200, description="Average heart rate during exercise (50-200)")
    Body_Temp: float = Field(..., gt=35, le=42, description="Body temperature in Celsius (35-42)")

class PredictionOutput(BaseModel):
    predicted_calories: float