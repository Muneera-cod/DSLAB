import matplotlib.pyplot as plt
x=[10,20,30]
y=[20,40,10]
plt.plot(x,y,label='line 1',color='violet',linewidth=3,marker='o',markerfacecolor='red')
h=[10,20,30]
z=[40,10,30]
plt.plot(h,z,label='line 2',color='yellow',marker='.',markersize='12',markerfacecolor='black')
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.title('Two or more lines on same plot with suitable legends')
plt.legend()
plt.show()