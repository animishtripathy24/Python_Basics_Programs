def checkEven(n):
    if(n&1):
        return "It is not a Even Number"
    else:
        return "It is a Even Number"


n=int(input("Enter the value of n "))
a=checkEven(n)
print(a)
