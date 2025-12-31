from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import joblib
import pandas as pd

# 1. Initialize the App
app = FastAPI(
    title="California Housing Price Prediction",
    description="API to predict housing prices based on features like location, rooms, and ocean proximity."
)

# 2. Load the Model (The "Kitchen")
# We load it once when the server starts so we don't waste time reloading it for every request.
try:
    model = joblib.load("model/housing_model.pkl")
    print("✅ Model loaded successfully!")
except Exception as e:
    print(f"❌ Error loading model: {e}")
    model = None

# 3. Define the Input Schema (The "Menu")
# This tells the user exactly what data they need to send.
class HousingFeatures(BaseModel):
    longitude: float
    latitude: float
    housing_median_age: float
    total_rooms: float
    total_bedrooms: float
    population: float
    households: float
    median_income: float
    ocean_proximity: str 

# 4. Define the Prediction Endpoint
@app.post("/predict")
def predict_price(features: HousingFeatures):
    if model is None:
        raise HTTPException(status_code=500, detail="Model is not loaded.")
    
    # Convert the input data (Pydantic object) to a Pandas DataFrame
    # Scikit-learn models expect a DataFrame with column names
    input_df = pd.DataFrame([features.dict()])
    
    try:
        # Make the prediction
        prediction = model.predict(input_df)
        
        # Return the result
        return {
            "predicted_median_house_value": float(prediction[0])
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# 5. Health Check
@app.get("/health")
def health_check():
    return {"status": "ok", "model_loaded": model is not None}