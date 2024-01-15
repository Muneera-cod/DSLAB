import numpy as np
List=[1,2,3,4,5]
Array=np.array(List)
file=open('oiu.txt',"w+")
content=str(Array)
file.write(content)
file.close()

file=open('oiu.txt',"r")
content=file.read()
file.close()
print(content)