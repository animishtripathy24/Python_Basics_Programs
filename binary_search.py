def binarySearch(arr,low,high,target):
    if(low <= high):
        mid=(low+high)>>1
        if(arr[mid]== target):
            return mid
        elif(target<arr[mid]):
            return binarySearch(arr,low,mid-1,target)
        else:
            return binarySearch(arr,mid+1,high,target)
    else:
        return -1
n=int(input("Enter the size of the array"))
arr=[]
for i in range(0,n):
    c=int(input())
    arr.append(c)
low=0
high=n-1
target=int(input("Enter the target value too be searched"))
pos=binarySearch(arr,low,high,target)
if(pos==-1):
    print("The given target was not found in the array")
else:
    print("The target element was found at the position",pos)
