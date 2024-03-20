# if the sum of all the individual digits and product of all individual digits are equal ,
#then we can say that the number is a spy number.

#example=1124,132   1+1+2+4=9,  1*1*2*4=9

#steps:

#find individual digits n%10
#reduce the number  n//10(for python)
#sum and product of all the individual digits.

#another method

#n='123'
#for i in n:
#sum+=int(i)
#product+=int(i)

n=int(input("enter value of n"))
sum=0
prod=1
temp=n
while(n>0):
    digit=n%10
    sum=sum+digit
    prod=prod*digit
    n=n//10
if sum==prod:
    print(temp,"is a SPY NUMBER")
else:
    print(temp,"is NOT SPY NUMBER")
