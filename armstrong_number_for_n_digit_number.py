n=int(input("enter the value for n"))
t=n
temp=n
sum=0
count=0
while(n!=0):
    digit=n%10
    count=count+1
    n=n//10
while(t!=0):
    rem=t%10
    sum=sum+pow(rem,count)
    t=t//10
if(sum==temp):
    print(temp,"is a armstrong number")
else:
    print(temp,"is not an armstrong number")
    
            
