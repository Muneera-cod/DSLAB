import pandas as pd
data=([1,2,3],[4,5,6],[5,6,7],[9,1,2])
s=pd.Series(data,index=['x','y','z','h'])
print(s)
print(s['x'])
a={'day1':345,'day2':400,'day3':280}
datas=pd.Series(a)
print(datas)