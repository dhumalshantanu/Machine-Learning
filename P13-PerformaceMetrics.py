from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from sklearn.metrics import confusion_matrix
from sklearn.metrics import mean_squared_error, mean_absolute_error
import numpy as np

y_true = [1, 1, 0, 1, 0, 0, 0, 1, 1] # What actully happned

y_predicted = [1, 0, 1, 0, 0, 0, 1, 1, 1] # What model predicted

print("Accuracy : ", accuracy_score(y_true, y_predicted))
print("Precision : ", precision_score(y_true, y_predicted))
print("Recall : ", recall_score(y_true, y_predicted))
print("F1 Score : ", f1_score(y_true, y_predicted))

cm = confusion_matrix(y_true, y_predicted)
print("Confusion Matrix : ")
print(cm)

mae = mean_absolute_error(y_true, y_predicted)
mse = mean_squared_error(y_true, y_predicted)
rmse = np.sqrt(mse)

print("MAE : On average off by : ", mae)
print("MSE : Squared Mistake Value : ", mse)
print("RMSE : Final Realistic Error : ", rmse)

