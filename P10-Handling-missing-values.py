import pandas as pd
import numpy as np

# ---------------------------------------
# STEP 1: Create a Sample DataFrame
# ---------------------------------------

data = {
    "Name": ["Amit", "Neha", "Rahul", None, "Pooja"],
    "Age": [22, 25, None, 23, None],
    "Marks": [85, None, 78, 90, None],
    "City": ["Pune", "Mumbai", None, "Delhi", "Pune"]
}

df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)
print("\n")

# ---------------------------------------
# STEP 2: Check Missing Values
# ---------------------------------------

print("Check missing values (True means missing):")
print(df.isnull())
print("\n")

print("Count of missing values in each column:")
print(df.isnull().sum())
print("\n")

# ---------------------------------------
# METHOD 1: Drop Rows with Missing Values
# ---------------------------------------

df_drop_rows = df.dropna()

print("After dropping rows with missing values:")
print(df_drop_rows)
print("\n")

# ---------------------------------------
# METHOD 2: Drop Columns with Missing Values
# ---------------------------------------

df_drop_columns = df.dropna(axis=1)

print("After dropping columns with missing values:")
print(df_drop_columns)
print("\n")

# ---------------------------------------
# METHOD 3: Fill Missing Values with a Constant
# ---------------------------------------

df_fill_constant = df.fillna("Unknown")

print("After filling missing values with a constant:")
print(df_fill_constant)
print("\n")

# ---------------------------------------
# METHOD 4: Fill Missing Numerical Values with Mean
# ---------------------------------------

df_mean = df.copy()
df_mean["Age"] = df_mean["Age"].fillna(df_mean["Age"].mean())
df_mean["Marks"] = df_mean["Marks"].fillna(df_mean["Marks"].mean())

print("After filling missing numerical values with mean:")
print(df_mean)
print("\n")

# ---------------------------------------
# METHOD 5: Fill Missing Values with Median
# ---------------------------------------

df_median = df.copy()
df_median["Age"] = df_median["Age"].fillna(df_median["Age"].median())
df_median["Marks"] = df_median["Marks"].fillna(df_median["Marks"].median())

print("After filling missing numerical values with median:")
print(df_median)
print("\n")

# ---------------------------------------
# METHOD 6: Fill Missing Values with Mode
# ---------------------------------------

df_mode = df.copy()

for column in df_mode.columns:
    df_mode[column] = df_mode[column].fillna(df_mode[column].mode()[0])

print("After filling missing values with mode:")
print(df_mode)
print("\n")

# ---------------------------------------
# METHOD 7: Forward Fill (ffill)
# ---------------------------------------

df_ffill = df.fillna(method="ffill")

print("After forward fill:")
print(df_ffill)
print("\n")

# ---------------------------------------
# METHOD 8: Backward Fill (bfill)
# ---------------------------------------

df_bfill = df.fillna(method="bfill")

print("After backward fill:")
print(df_bfill)
print("\n")

# ---------------------------------------
# STEP 3: Final Notes
# ---------------------------------------
# Mean / Median: Best for numerical data
# Mode: Best for categorical data
# ffill / bfill: Useful for time-series data
# dropna: Use only when data loss is acceptable
