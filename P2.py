import pandas as pd
import datetime
from datetime import date

data = pd.read_csv("Practice_Data.csv")
print(data.head())

print(data.dtypes)
print("Total Null values : ")
print(data.isnull().sum())

data = data.dropna(subset = ["Date"])

print(data.isnull().sum())

data["Calories"] = data["Calories"].fillna(data["Calories"].mean())
print(data.isnull().sum())

data['Date'] = pd.to_datetime(data['Date'])

print(data)