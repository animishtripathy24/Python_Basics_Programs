#WAP TO FIND NEON NUMBER

#STEPS:
#SQUARE OF A NUMBER
#SUM OF INDIVIDUAL DIGITS OF A SQUARE
#COMPARE SUM WITH THE NUMBER
#EXAMPLE N=9 SQUARE IS 81 AND SUM OF 8 AND 1 IS 9 THEN 9 IS A NEON NUMBER

n=int(input("enter value for n"))
sqr=n**2
sum=0
while sqr>0:
    digit=sqr%10
    sum=sum+digit
    sqr=sqr//10
if(sum==n):
    print(n,"is Neon number")
else:
    print(n,"is not Neon number")
