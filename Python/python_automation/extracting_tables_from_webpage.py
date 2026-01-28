import pandas as pd
kings=pd.read_html("https://haydenrue.com/nepal/kings-of-nepal/")
print(kings)
table=kings[0]
table.to_csv("Kings_of_nepla.txt",index=False, sep="\t")
print("Table saved")