from sklearn.tree import DecisionTreeClassifier

x = [
    [7, 2],
    [8, 3],
    [9, 8],
    [10, 9]
]

y = [0, 0, 1, 1]

model = DecisionTreeClassifier()

model.fit(x, y)

size = float(input(f"Enter the size of the fruit in cm : "))
shade = float(input(f"Enter the shade of the fruit between 0 to 1 : "))

result = model.predict([[size, shade]])[0]

if result == 0:
    print("Apple")
else :
    print("Orange")