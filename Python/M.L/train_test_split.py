from sklearn.preprocessing import StandardScaler, MinMaxScaler
from sklearn.model_selection import train_test_split
import pandas as pd
data={
    "StudyHours":[4,5,6,7,8],
    "TestScore":[50,60,70,80,90]
}
df=pd.DataFrame(data)
X=df[["StudyHours"]]
Y=df[["TestScore"]]
X_train, X_test, Y_train,Y_test=train_test_split(X,Y,test_size=0.2,random_state=42)

print("Training Data: ")
print(X_train)
print("Test Data")
print(X_test)
print(Y_train)
print(Y_test)











'''standard_scaler=StandardScaler()
standard_scaled=standard_scaler.fit_transform(df)
print("Standard Scaled")

print(pd.DataFrame(standard_scaled,columns=["StudyHours","TestScore"]))
minmax_scaler=MinMaxScaler()
minmax_scaled=minmax_scaler.fit_transform(df)
print("Min_Max_Scaled")
print(pd.DataFrame(minmax_scaled,columns=["StudyHours","TestScore"]))'''