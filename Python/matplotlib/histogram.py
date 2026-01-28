import matplotlib.pyplot as plt
import pandas as pd
data=pd.read_csv("game_sales_updated.csv")
plt.hist(data["Year"])
plt.show()