from sklearn.preprocessing import LabelEncoder
import pandas as pd

df = pd.read_csv(r"C:\Users\Shantanu\Desktop\Machine Learning\Machine-Learning\Practice_Data.csv")
print(df)

df_lable = df.copy()

le = LabelEncoder()
df_lable['Gender_encoded'] = le.fit_transform(df_lable['Gender'])

print('\nLabeled Encoded Data')
print(df_lable)