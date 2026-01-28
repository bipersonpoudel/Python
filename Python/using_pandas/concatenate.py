import pandas as pd
region1={
    "Id":[101,102],
    "Name":["Bipson","Bikash"],
    "Age":[18,12]
}
region2={
    "Id":[103,104],
    "Name":["Bishesh","Bibash"],
    "Age":[23,11]
}
df__region1=pd.DataFrame(region1)
df__region2=pd.DataFrame(region2)

concatenated=pd.concat([df__region1,df__region2],axis=0,ignore_index=True)
print(concatenated)