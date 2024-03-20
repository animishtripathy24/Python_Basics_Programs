n=int(input("enter the value of n"))
sum=0
while(n!=0):
    rem=n%10;
    sum=sum+rem;
    n=n//10;
print("the sum of all digits of the number is ",sum)
