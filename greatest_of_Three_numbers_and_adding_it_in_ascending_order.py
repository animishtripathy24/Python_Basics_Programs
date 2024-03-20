a=int(input())
b=int(input())
c=int(input())
if(a>b and a>c):
    print("The greatest of three numbers is: ",a)
elif(b>c):
    print("The greatest of three numbers is :",b)
else:
    print("The greatest of three numbers is : ",c)

if(a<b and a<c):
    if(b<c):
        min,mid,max=a,b,c
    else:
        min,mid,max=a,c,b
elif(b<a and b<c):
    if(a<c):
        min,mid,max=b,a,c
    else:
        min,mid,max=b,c,a
else:
    if(a<b):
        min,mid,max=c,a,b
    else:
        min,mid,max=c,b,a
print("The sum of the numbers in ascending order")
print("1-> ",min)
print("2-> ",min+mid)
print("3-> ",min+mid+max)
print("The final sum is : ",min+mid+max)
