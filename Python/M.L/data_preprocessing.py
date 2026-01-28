import pandas as pd
data={
    "Name":["Paras","Lalit","Sandeep","Karan","Lalit"],
    "Age":[30,45,None,27,None],
    "Salary":[300000,40000,None,50000,None]

}


df=pd.DataFrame(data)
print("Original Data")
print(df)
print(df.isnull().sum())
df_drop=df.dropna()
print("Modified_Data")
print(df_drop)
df["Age"].fillna(df["Age"].mean(),inplace= True)
df["Salary"].fillna(df["Salary"].mean(),inplace= True)
print(df)
