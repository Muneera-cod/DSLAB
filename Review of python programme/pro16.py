import matplotlib.pyplot as plt
import numpy as np
a=np.array(['Java','Python','PHP','JavaScriot','C#','C++'])
b=np.array([22.2,17.6,8.8,8,7.7,6.7])
plt.bar(a,b)
plt.xlabel('Popularity')
plt.ylabel('Programming Language')
plt.show()
plt.barh(a,b,color='red')
plt.xlabel('Popularity')
plt.ylabel('Programing Language')
plt.show()
plt.bar(a,b,color=['red','blue','yellow','violet','purple','indigo'])
plt.xlabel('Popularity')
plt.ylabel('Programing Language')
plt.show()

la=['Java','python','Php','JavaScript','C#','C++']
plt.pie(b,labels=la)
plt.legend()
plt.show()
plt.hist(b,bins=10)
plt.show()