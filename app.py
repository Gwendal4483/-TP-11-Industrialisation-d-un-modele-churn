import joblib
import pandas as pd
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()
model = joblib.load("model/churn_pipeline.pkl")

class Client(BaseModel):
    tenure: int
    MonthlyCharges: float
    Contract: str
    InternetService: str

@app.get("/")
def home():
    return {"message": "API OK"}

@app.post("/predict")
def predict(client: Client):
    df = pd.DataFrame([{
        "tenure": client.tenure,
        "MonthlyCharges": client.MonthlyCharges,
        "Contract": client.Contract,
        "InternetService": client.InternetService
    }])
    pred = model.predict(df)
    return {"prediction": int(pred[0])}