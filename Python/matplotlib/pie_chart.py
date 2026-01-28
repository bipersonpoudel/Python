import matplotlib.pyplot as plt
import pandas as pd
data=pd.read_csv("game_sales_updated.csv")

sales_data=data[["Sales_Australia","Sales_Asia","Sales_Europe","Sales_SouthAmerica","Sales_NorthAmerica"]]
overall_sales_data=sales_data.T.sum(axis="columns")
plt.pie(overall_sales_data,labels=overall_sales_data.index,startangle=90)
plt.show()