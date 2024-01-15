import pandas as pd
dataframe=pd.read_csv('27.txt')
print(dataframe)
o=dataframe.iloc[1:,]
print(o)