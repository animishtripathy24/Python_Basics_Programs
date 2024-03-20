def pattern_6(n):
    i=1
while(i<=n):
    j=n-i+1
    x=n-i+1;
    while(j):
        print(x,end=' ')
        j=j-1
        x=x-1
    i=i+1
    print("\n")

def pattern_7(n):
    i=1
while(i<=n):
    j=1
    x=n-i;
    while(j<=i):
        print(x,end=' ')
        j=j+1
        x=x-1
    i=i+1
    print("\n")
    
n=int(input("Enter the number of rows"))
print(pattern_6(n))
print(pattern_7(n))
    
    
