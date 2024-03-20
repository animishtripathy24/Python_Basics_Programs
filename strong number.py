#logic of the program- if the sum of  factorial of individiul digits of a number is equal to that number then that number is called strong number
n=int(input("enter the value of n"))
temp=n
sum=0
while n>0:
    digit=n%10
    fact=1
    print("digits:",digit)
    for i in range(1,digit+1):
        fact=fact*i
        print("factorial",fact)
        sum+=fact
        print("sum=",sum)
        n=n/10
if sum==temp:
    print(temp,"is a strong number")
else:
    print(temp,"is not a strong number")
