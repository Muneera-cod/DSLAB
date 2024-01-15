import pandas as pd
d={'col1':[1,2,3],'col2':[4,5,6]}
df=pd.DataFrame(d)
print(df)
Col_count=df.shape[1]
Row_count=df.shape[0]
print(Col_count," is the number of coloum")
print(Row_count," is the number of row")