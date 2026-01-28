from sklearn.preprocessing import StandardScaler, MinMaxScaler
import pandas as pd
data={
    "StudyHours":[4,5,6,7,8],
    "TestScore":[50,60,70,80,90]
}
df=pd.DataFrame(data)
standard_scaler=StandardScaler()
standard_scaled=standard_scaler.fit_transform(df)
print("Standard Scaled")

print(pd.DataFrame(standard_scaled,columns=["StudyHours","TestScore"]))
minmax_scaler=MinMaxScaler()
minmax_scaled=minmax_scaler.fit_transform(df)
print("Min_Max_Scaled")
print(pd.DataFrame(minmax_scaled,columns=["StudyHours","TestScore"]))