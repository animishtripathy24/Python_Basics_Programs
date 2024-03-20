#WAP TO FIND PRONIC NUMBER PROGRAM IN PYTHON

# The product of two consecutive number is equal to that number.example- 1) 6=2*3    2)12=3*4   3)20=4*5
# logic: we have to iterate from 1 to n+1 and the multiplying as n*(n+1)==n and the break.

n=int(input("enter the value of n"))
flag=0
for i in range(1,n+1):
    if (i*(i+1)==n):
        flag=1
        break
if flag==1:
    print(n,"is a PRONIC NUMBER")
else:
    print(n,"is not an PRONIC NUMBER")
    
