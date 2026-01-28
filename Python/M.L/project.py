'''
3 Step formula for machine laarning

1 --> Are x & y numeric.
    use scatter plot for showing relationships

2  --> Is one column a category.
    use bar/count plot


3 --> Want to see a distribution shape
    Use histogram plot/ kde plot/ box plot


'''


import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error
import numpy as np
import matplotlib.pyplot as plt
data=pd.read_csv("D:/Python/archive/student_performance_analysis.csv")
x=data[['hours_studied']]
y=data['test_score']
model=LinearRegression()
model.fit(x,y)
predicted_scores=model.predict(x)
#print(predicted_scores)

mae=mean_absolute_error(y,predicted_scores)
mse=mean_squared_error(y,predicted_scores)
rmse=np.sqrt(mse)

print("Mean Absolute Error :",round(mae,2))
print("Mean Squared Error :",round(mse,2))
print(" Root Mean Squared Error :",round(rmse,2))


plt.figure(figsize=(10,6))
plt.hist(data["test_score"],bins=30,color="skyblue",edgecolor="black")
plt.title("Test Score")
plt.xlabel("Final Exam Score")
plt.ylabel("No of Student ")
plt.grid(True)
plt.show()