a=int(input("enter value of a="))
b=int(input("enter value of b="))
c=int(input("enter value of c="))
if a>b:
    if a>c:
        print("first number=",a)
    else:
        print("third number=",c)
else:
    if b>c:
        print("second number=",b)
    else:
         print("third number=",c)
