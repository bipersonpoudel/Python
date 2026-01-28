import matplotlib.pyplot as plt
import pandas as pd
data = pd.read_csv("D:/Python/matplotlib/game_sales_updated.csv", encoding="utf-8")
print(data["Genre"].unique())
count=data["Genre"].value_counts()
print(count)
x_bar=count.index
y_bar=count.values
plt.figure(figsize=(8,6))
plt.bar(x_bar,y_bar,width=0.5)
plt.xlabel("Genre")
plt.ylabel("Count")

plt.show()