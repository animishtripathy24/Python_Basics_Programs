def linearSearch(arr,target):
    for i in range(0,len(arr)):
        if(arr[i]==target):
            return i
    return -1
n=int(input("Enter the size of the array"))
arr=[]
print("Populate the array",end='\n')
for i in range(0,n):
    c=int(input())
    arr.append(c)
target=int(input("Enter the target value too be searched"))
if(linearSearch(arr,target)==-1):
    print("NOT FOUND IN THE ARRAY")
else:
    print("FOUND IN THE ARRAY IN THE POSITION-> ",linearSearch(arr,target))
