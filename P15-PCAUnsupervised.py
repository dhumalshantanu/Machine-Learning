import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

data = {
    "Age" : [27, 34, 25, 45, 23, 35],
    "Income" : [30000, 50000, 20000, 60000, 80000, 40000],
    "Spending" : [70, 50, 20, 30, 40, 10],
    "Savings" : [1000, 4000, 3000, 2000, 5000, 6000]
}

df = pd.DataFrame(data)
scaler = StandardScaler()
scaled_data = scaler.fit_transform(df)

pca = PCA(n_components = 2)
pca_result = pca.fit_transform(scaled_data)
pca_df = pd.DataFrame(pca_result, columns = ["PCA1", "PCA2"])
explained_variance = pca.explained_variance_ratio_
print("Varience Captured by each PCA Component : ")
print(np.round(explained_variance * 100, 2))

plt.figure(figsize = (8, 6))
plt.scatter(pca_df["PCA1"], pca_df["PCA2"], color = "Black")
plt.title("PCA Projection 2D view : ")
plt.xlabel("PCA1 Main Pattern")
plt.ylabel("PCA2 Minor Pattern")
plt.grid(True)
plt.show()

print("New Data With PCA : ")
print(pca_df)
