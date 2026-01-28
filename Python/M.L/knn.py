from sklearn.neighbors import KNeighborsClassifier
x=[
    [180,7],
   [200,7.5],
   [250,8],
   [300,8.5],
   [350,9],
   [400,9.5]
   ]
y=[0,0,0,1,1,1]
model=KNeighborsClassifier(n_neighbors=3)
model.fit(x,y)
weight=float(input("Enter the weight: "))
size=float(input("Enter the size: "))
prediction=model.predict([[weight,size]])[0]
if prediction==0:
    print("It is likely to be an apple.")
else:
    print("It is likely to be an orange")
