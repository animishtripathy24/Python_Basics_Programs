import numpy as np
m=int(input("enter rows or columns"))
ar=np.empty((m,m),dtype=np.int8)
print("ENTER DATA FOR THE FIRST MATRIX")
s1=s2=0
for i in range(m):
    for j in range (m):
        ar[i,j]=int(input("enter numbers"))
        if(i==j):
            s1=s1+ar[i,j]
        if((i+j)==(m-1)):
            s2=s2+ar[i,j]
print("THE FIRST MATRIX IS--")
for i in range(m):
    for j in range(m):
        print(ar[i,j],end=" ")
    print()
print("sum of the left diagonals",s1)
print("sum of the right diagonals",s2)
