s=input("enter a word")
l=len(s)
r=""
for i in range(l):
    c=s[i]
    r=c+r
if r==s:
    print("the string is palindrome")
else:
    print("the string is not palindrome")
