import matplotlib.pyplot as plt
with open('test.txt') as f:
 data=f.read()
 print(data)
 data=data.split('\n')

print(data)
x=[row.split(',')[0] for row in data]
y=[row.split(',')[1] for row in data]
print()
print()
print(x)
print()
print(y)
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Simple Graph')
plt.plot(x,y,color='red')
plt.show()