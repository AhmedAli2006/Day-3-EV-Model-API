from fastapi import FastAPI
from app.schemas import EVInput
import joblib
import numpy as np

# Load model
model = joblib.load("models/ev_demand_catboost.joblib")

app = FastAPI(title="EV Demand Prediction API", version="1.0")

@app.get("/")
def home():
    return {"message": "EV Demand Prediction API is running!"}

@app.post("/predict")
def predict(data: EVInput):
    features = np.array([[data.Site, data.CP_ID, data.Connector_Type,
                          data.Duration_hours, data.hour, data.day_of_week,
                          data.month, data.Postcode]])
    prediction = model.predict(features)[0]
    return {"Predicted_Consumption_kWh": float(prediction)}

