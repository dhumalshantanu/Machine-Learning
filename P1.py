import pandas as pd

data = {
    "Name" : ["Shantanu", "Sarthak", "Shivaji", "Niranjan", "Om"],
    "Age" : [22, None, 23, 22, None],
    "Salary" : [4000, 5000, 4000, None, 5000]
}

df = pd.DataFrame(data)
print("Original Data Frame")
print(df)

print(df.isnull().mean() * 100)

print(df.isnull(). sum())
df_drop = df.dropna()
print(df_drop)

df["Age"].fillna(df["Age"].mean(), inplace = True)
df["Salary"].fillna(df["Salary"].mean(), inplace = True)
print(df)

print(df.isnull().mean() * 100)