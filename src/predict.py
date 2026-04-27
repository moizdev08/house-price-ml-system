import joblib
import numpy as np
import os

#Load model
base_dir=os.path.dirname(os.path.dirname(__file__))
model_path=os.path.join(base_dir,"models","model.pkl")

model=joblib.load(model_path)

def predict_price(features:list):
    features_array=np.array(features).reshape(1,-1)
    prediction=model.predict(features_array)
    return float(prediction[0])