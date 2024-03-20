#WAP TO FIND STRONG NUMBER

#if the sum of factorial of individual digits is equal to that given number then the given number is known as strong number
#example=145

#steps involved

#identify individual digits
#find factorial for digits
#sum of all factorial of individual digits

n=int(input("enter value for n"))
sum=0
temp=n
fact=1
while(n>0):
    digit=n%10
    for i in range(1,digit+1):
        fact=fact*i
        sum=sum+fact
    n=n//10
if sum==temp:
    print(temp,"is a strong number")
else:
    print(temp,"is not a strong number")
