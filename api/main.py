import logging
logging.basicConfig(level=logging.INFO)
from fastapi import FastAPI
from fastapi import HTTPException
from pydantic import BaseModel,Field
from src.predict import predict_price

app=FastAPI()

class HouseFeatures(BaseModel):
    bedrooms:int=Field(...,gt=0,lt=20)
    bathrooms:int=Field(...,gt=0,lt=20)
    area:float=Field(...,gt=100)
    age:int=Field(...,ge=0,le=100)

@app.get("/")
def home():
    return {"message":"House Price Predition API is running"}

@app.post("/predict")
def predict(data:HouseFeatures):
    try:
        logging.info(f"Recieved input:{data}")

        features=[
        data.bedrooms,
        data.bathrooms,
        data.area,
        data.age
        ]
    
        price=predict_price(features)
    
        return{
            "status":"success",
            "predicted_price":price
        }

    except  Exception as e:
        logging.error(f"Error occured: {str(e)}")
        raise HTTPException(status_code=500,detail="Internal server error")
    

