import pandas as pd
data={
    "Name":["Biperson","Bishnu","Krishna","Ram","Hari","Shyam","Shiva","Mahadev"],
    "Age":[10,20,30,40,45,23,45,29],
    "City":["kathmandu","Pokhara","Kushma","Baglung","Beni","Chitwan","Bharatpur","Muglin"],
    "Performance Score":[93,90,56,66,89,88,45,86]


}
df=pd.DataFrame(data)
print("Sample Data")
print(df)

print(df["Name"])
print("Printing_Filtered_Rows")
filtered_row=df[df["Age"]>30]
print(filtered_row)
print("Selecting Multiple Comdition")
selection_using_multiple_cond=df[(df["Age"]>20)&(df["Performance Score"]>50)]
print(selection_using_multiple_cond)


#print(f'"Selecting Names: {df["Name"]}')