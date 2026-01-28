import pandas as pd
data={
    "Name":["Biperson","Bishnu","Krishna","Ram","Hari","Shyam","Shiva","Mahadev"],
    "Age":[10,20,30,40,45,23,45,29],
    "City":["kathmandu","Pokhara","Kushma","Baglung","Beni","Chitwan","Bharatpur","Muglin"],
    "Performance Score":[93,90,56,66,89,88,45,86],
    "Salary":[98000,76542,25755,76444,87543,67890,46544,67543]


}
df=pd.DataFrame(data)

print(df)
print("Adding a new column named bonus")
df["Bonus"]= df["Salary"]*0.1
print(df)
#Using insert method
df.insert(0,"Id.No",[101,102,103,104,105,106,107,108])
print(df)