import pandas as pd
data={
    "Name":["Biperson","Bishnu","Krishna","Ram","Hari","Shyam","Shiva","Mahadev"],
    "Age":[10,None,30,40,45,23,45,29],
    "City":["kathmandu","Pokhara","Kushma","Baglung","Beni","Chitwan","Bharatpur","Muglin"],
    "Performance Score":[93,None,56,66,89,88,45,86],
    "Salary":[98000,None,25755,76444,87543,67890,46544,67543]


}
df=pd.DataFrame(data)
print(df)
'''df.dropna(axis=0,inplace=True)
print(df)'''

df.fillna({"Age":df["Age"].mean()}, inplace=True)
df.fillna({"Performance Score":df["Performance Score"].mean()}, inplace=True)
print(df)