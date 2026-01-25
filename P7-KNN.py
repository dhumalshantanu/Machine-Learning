from sklearn.neighbors import KNeighborsClassifier

x = [
    [180, 7],
    [200, 7.5],
    [220, 8],
    [240, 8.5],
    [260, 9],
    [280, 9.5]
]

y = [0, 0, 0, 1, 1, 1]

model = KNeighborsClassifier(n_neighbors = 3)

model.fit(x ,y)

weight = float(input("Enter the weight of the Fruit in gm : "))
size = float(input("Enter the size of the fruie in cm : "))

prediction = model.predict([[weight, size]])[0]

if prediction == 0:
    print("The Fruite might be an APPLE : ")
else : 
    print("The Fruite might be an ORANGE : ")


