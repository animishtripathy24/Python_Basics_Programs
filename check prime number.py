n=int(input("enter value of n"))
f=0
for i in range(1,n+1):
    r=n%i
    if(r==0):
        f=f+1
if(f==2):
    print("THE NUMBER IS PRIME")
else:
    print("THE NUMBER IS NOT PRIME NUMBER")
    
