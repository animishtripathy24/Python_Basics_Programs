import numpy as np
m=int(input ("enter number of rows"))
n=int(input("enter number of columns"))
ar1=np.empty([m,n],dtype=np.int8)
ar2=np.empty([m,n],dtype=np.int8)
ar3=np.empty([m,n],dtype=np.int8)
print("ENTER DATA IN THE FIRST MATRIX")
for i in range(m):
    for j in range(n):
        ar1[i,j]=int(input("enter numbers"))
print("ENTER DATA FOR SECOND MATRIX")
for i in range(m):
     for j in range(n):
         ar2[i,j]=int(input("enter numbers"))
# SUM OF THE ABOVE TWO MATRIX
for i in range(m):
    for j in range(n):
     ar3[i,j]=ar1[i,j]+ar2[i,j]
print("the first matrix is -")
for i in range(m):
     for j in range(n):
         print(ar1[i,j],end=" ")
     print()
print("the second matrix is -")
for i in range(m):
    for j in range(n):
        print(ar2[i,j],end=" ")
    print()
print("the sum of the above two matrix is -")
for i in range(m):
    for j in range(n):
        print(ar3[i,j],end=" ")
    print()    
    
        
        

        

     


