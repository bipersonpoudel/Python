import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
data= pd.read_csv("game_sales_updated.csv")
'''sns.histplot(data["Year"])
plt.show()
'''
sns.kdeplot(data["Year"])
plt.show()

