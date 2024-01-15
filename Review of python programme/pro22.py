import pandas as pd
datas=pd.read_csv('test.txt')
print(datas)
dataframe_sorted=datas.sort_values(by=['Name','Rollno'])
print(dataframe_sorted)