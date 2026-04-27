import pandas as pd

df=pd.read_csv("data/housing.csv")


print("First 5 rows:")
print(df.head())

print("\nColumns:")
print(df.columns)

print("\nData Info:")
print(df.info())