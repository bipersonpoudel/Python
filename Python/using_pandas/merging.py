import pandas as pd
customer={
    "Id":[101,102,103,104],
    "Name":["Bipson","Bikash","Bishesh","Bibash"],
    "Age":[18,12,23,11]
    
}
order={
    "Id":[101,103,104],
    "Amoount":[100000,1222,453]
}
df_customer=pd.DataFrame(customer)
df_order=pd.DataFrame(order)
merged=pd.merge(df_customer,df_order,on="Id",how="left")
print(merged)
merged=pd.merge(df_customer,df_order,on="Id",how="right")
print(merged)