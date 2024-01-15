import pandas as pd
import matplotlib.pyplot as plt
data=[[2,'Adarsh',20],[1,'abhinav',24],[3,'amal',22]]
datas=pd.DataFrame(data,columns=['id','Name','Age'])
print(datas)
datas.plot()
plt.show()