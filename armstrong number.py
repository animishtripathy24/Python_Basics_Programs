# if the sum of the cubes of individual digits of a three digits number is equal to that number then that number is called an armstrong number
n=int(input("enter value of n="))
sum=0
while (n!=0):
    #finding individual digits
    d=n%10
    #finding sum of cubes of individual digits
    sum=sum+d*d*d
    #reducing the number
    n=int(n/10)
if(n==sum):
    print("number is an ARMSTRONG NUMBER")
else:
    print("number is not an ARMSTRONG NUMBER")
    
