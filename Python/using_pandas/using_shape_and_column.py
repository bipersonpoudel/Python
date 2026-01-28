import pandas as pd
data={
    "Name":["Biperson","Bishnu","Krishna","Ram","Hari","Shyam","Shiva","Mahadev"],
    "Age":[10,20,30,40,45,23,45,29],
    "City":["kathmandu","Pokhara","Kushma","Baglung","Beni","Chitwan","Bharatpur","Muglin"]


}
df=pd.DataFrame(data)
print(df)
print(f"Shape: {df.shape}")
print(f"Column Name: {df.columns}")