import pandas as pd

data ={
    "Name":["Biperson","Bipson","Krishna","Hari","Bisaj","Samir","kiran"],
    "Age":[18,12,7,67,14,16,17],
    "City":["Kathmandu","Pokhara","Kushma","Chitwan","Durlung","Biratnagar","Baglung"]
}

df=pd.DataFrame(data)
print(df)
df.to_csv("output.csv",index=False)
df.to_excel("output.xlsx",index=False)
df.to_json("output.json",index=False)
