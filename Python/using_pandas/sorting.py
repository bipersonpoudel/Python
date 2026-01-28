'''import pandas as pd
data={
    "Name":["Biperson","Bishnu","Nikash","Bishesh"],
    "Age":[10,23,32,12]
}
df=pd.DataFrame(data)
print("Before Sorting")
print(df)
print("After Sorting")
df.sort_values(by="Age", ascending=True,inplace=True)
print(df)'''

## Sorting for multiple values::
import pandas as pd



data={
    "Name":["Biperson","Bishnu","Nikash","Bishesh"],
    "Age":[10,23,32,12],
    "Salary":[10010,211123,1212,1231]
}
df=pd.DataFrame(data)
print("Before Sorting")
print(df)
print("After Sorting")
df.sort_values(by=["Age","Salary"], ascending=[True,False],inplace=True)
print(df)