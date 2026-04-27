import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import joblib
import os

#Load Dataset
base_dir=os.path.dirname(os.path.dirname(__file__))
file_path=os.path.join(base_dir,"data","housing.csv")

df=pd.read_csv(file_path)

#Features and target
X=df[["bedrooms","bathrooms","area","age"]]
y=df["price"]

#Split data
X_train,X_test,y_train,y_test=train_test_split(
    X,y,test_size=0.2,random_state=42
)

#Train model
model=LinearRegression()
model.fit(X_train,y_train)

#Save model
model_path=os.path.join(base_dir,"models","model.pkl")
joblib.dump(model, model_path)

print("Model trained and saved successfully!")