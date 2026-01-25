from sklearn.linear_model import LinearRegression

x = [[1], [2], [3], [4], [5]]
y = [40, 50, 60, 70, 80]

model = LinearRegression()

model.fit(x, y)

hours = float(input("Enter the NUmber of Hours you Studied : "))

predicted_marks = model.predict([[hours]])

print(f"Based on the number of hours you enterd, You may score around : {predicted_marks}")
