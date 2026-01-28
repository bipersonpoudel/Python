import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
data= pd.read_csv("game_sales_updated.csv")

sns.boxplot(data)
plt.xticks(rotation=90,fontsize=10)
plt.show()

