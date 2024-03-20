n=int(input("Enter the value of n "))

for i in range(n,0,-1):
    x=i
    for j in range(1,i+1):
        print(x,end=' ')
        x=x-1
    print("\n")
    
    
