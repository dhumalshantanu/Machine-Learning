from sklearn.preprocessing import LabelEncoder
import pandas as pd

df = pd.read_csv("student_dataset_50_rows.csv")
print(df)

df_encoded = pd.get_dummies(df, columns = ["City"])

print('\nLabeled Encoded Data')
print(df_encoded)