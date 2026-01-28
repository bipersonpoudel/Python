import pandas as pd
from sklearn.preprocessing import LabelEncoder
data=pd.read_csv("students_data.csv")
df=pd.DataFrame(data)

'''df_label=df.copy()
le=LabelEncoder()
df_label["Gender_Encoded"] = le.fit_transform(df_label["Gender"])
df_label["Passed Encoded"]=le.fit_transform(df_label["Passed"])
print("Encoded Data")
print(df_label[["Name","Passed Encoded","Gender_Encoded"]])'''


## ONE_HOT ENCOCDED DATA
df_encoded=pd.get_dummies(df,columns=["City"])
print(df_encoded)