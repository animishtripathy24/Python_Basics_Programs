import numpy as np
m=int(input("enter no of rows"))
n=int(input("enter no of coloumns"))
ar1=np.empty((m,n),dtype=np.int8)
ar2=np.empty((n,m),dtype=np.int8)
print("enter value for first matrix")
for i in range(m):
    for j in range(n):
        ar1[i,j]=int(input("enter numbers"))
for i in range(m):
    for j in range(n):
        ar2[j,i]=ar1[i,j]
print("the first matrix is--")
for i in range(m):
    for j in range(n):
        print(ar1[i,j],end=" ")
    print()
print("transpose of a matrix is--")
for i in range(n):
    for j in range(m):
        print(ar2[i,j],end=" ")
    print()        
