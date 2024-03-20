# write a program to find the super digit of a given number
# sum of individual digits of a given number must be single digit.
# then that digit is known as super digit of a given number.

n=int(input("enter the value of n"))
while n>=10:
    x=n
    sum=0
    while(x>0):
        r=x%10
        sum=sum+r
        x=x//10
    n=sum
print("super digit is",sum)
