def factorial(n): 
    if(n==0):
        return 1
    else:
        return n*factorial(n-1)


n=int(input("Enter the value of n"))
ans=factorial(n)
print("The factorial is ",ans)
