from sklearn.linear_model import LinearRegression
x=[[1],[2],[3],[4],[5]]
y=[40,45,56,68,79]
model=LinearRegression()
model.fit(x,y)
hours=float(input("How many Hours did you study "))
predicted_marks=model.predict([[hours]])
print(f"Based On your studied hours You may score {predicted_marks}")