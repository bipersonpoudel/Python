'''from sklearn.preprocessing import LabelEncoder
import pandas as pd
df=pd.read_csv("students_data.csv")
df_label=df.copy()
le=LabelEncoder()
df_label["Gender_Encoded"]=le.fit_transform(df["Gender"])
print(df_label)
'''



###TRAIN_TEST_SPLIT


from sklearn.model_selection import train_test_split
import pandas as pd
df=pd.read_csv("students_data.csv")
x=df[["Name"]]
y=df[["Gender"]]
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=42)
print("Training Data: ")
print(x_train)
print("Test Data:")
print(x_test)
print("Training Data: ")
print(y_train)
print("Test Data:")
print(y_test)