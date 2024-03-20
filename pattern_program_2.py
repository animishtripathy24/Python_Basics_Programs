n=int(input("enter the value of n"))
i=1;
while(i<=n):
    j=1;
    ch='A'+n-i;
    while(j<=i):
        printf(char(ch))
        ch=ch+1
        j=j+1
    print("\n")
    i=i+1
