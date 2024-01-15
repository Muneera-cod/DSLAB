import matplotlib.pyplot as plt
x=[12,14,16,18,20,22,24]
y=[100,200,250,400,300,350,500]
plt.xlabel('Temperature in Degree Celsius')
plt.ylabel('Sales')
plt.xlim(10,30)
plt.ylim(0,520)
plt.plot(x,y,color='red',linestyle='dashed',linewidth=2,marker='.',markersize=12,markerfacecolor='black')

plt.show()
