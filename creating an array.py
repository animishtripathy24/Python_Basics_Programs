import numpy as np
n=int(input("enter value="))
ar=np.empty((n,),dtype=np.int8)
for i in range(n):
    ar[i]=int(input("enter value"))
print("elements of an array are=")
for i in range(n):
    print(ar[i])
                    
