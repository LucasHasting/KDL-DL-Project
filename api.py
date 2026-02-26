#Name:          Lucas Hasting
#Class:         MA 395
#Date:          ~/~/~
#Instructor:    Dr. Terwilliger
#Description:   Course Project - API for using DT model in legacy system
#               geeksforgeeks.org/python/fastapi-uvicorn/#:~:text=Last%20Updated%20:%2023%20Jul%2C%202025,server%20interface%20for%20asynchronous%20frameworks.

from fastapi import FastAPI #pip install fastapi uvicorn[standard]
import joblib
from pydantic import BaseModel
from typing import List

#uvicorn api:app => for api in folder loc

class Payload(BaseModel):
    data: List[float]

#load in DT model
model = joblib.load("DT.pkl")

#create a FastAPI instance
app = FastAPI()

#route for model prediction
@app.post("/predict")
def predict(payload: Payload):
    data = payload.data
    result = model.predict([data])
    return {"prediction": result[0]}
