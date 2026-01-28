from sklearn.linear_model import LogisticRegression
x=[[1],[2],[3],[4],[5]]
y=[0,0,1,1,1]
model=LogisticRegression()
model.fit(x,y)
hours=float(input("How many hours did you study? "))
result=model.predict([[hours]])[0]
if result==1:
    print(f"Based On your Studied Hour You are likely to pass")

else:
    print(f"Based On your Studied Hour You are likely to Fail")
