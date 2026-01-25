from sklearn.linear_model import LogisticRegression

x = [[1], [2], [3], [4], [5]]
y = [0, 0, 1, 1, 1]

model = LogisticRegression()
model.fit(x, y)

hours = float(input("Enter the NUmber of hours you Studied : "))
result = model.predict([[hours]])[0]

if result == 1:
    print(f"Based on {hours} hrs you studied, You are Likely to PASS : ")
else : 
    print(f"Based on {hours} hrs you studied, You are Likely to FAIL : ")