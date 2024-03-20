n=int(input("enter the value for n"))
sum=0
while(n!=0):
    #extracting individual digits
    digit=n%10
    print("digits",digit)
    #finding the sum of individual digits
    sum=sum+digit
    print("sum",sum)
    #reducing the number
    n=n//10
print("the sum of the individual digits of a given number is",int(sum))    
            
