'''import pandas as pd
import matplotlib.pyplot as plt
data=pd.read_csv("game_sales_updated.csv")
#print(data.head())
x_index=data["Year"].unique()
total=data["Year"].value_counts()
print(total)
print(x_index)

'''
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("game_sales_updated.csv")

# List of sales columns
sales_cols = [
    "Sales_Asia",
    "Sales_Europe",
    "Sales_SouthAmerica",
    "Sales_NorthAmerica",
    "Sales_Australia"
]
# Group by year and sum total sales
total_sales_by_year = data.groupby("Year")[sales_cols].sum().sum(axis=1)

print(total_sales_by_year)

# Plot
plt.figure(figsize=(12,6))
plt.bar(total_sales_by_year.index, total_sales_by_year.values)
plt.xlabel("Year")
plt.ylabel("Total Sales (All Regions Combined)")
plt.title("Total Game Sales per Year")
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()
