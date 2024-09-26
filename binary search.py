num=int(input())
a=[]
for i in range (num):
    m=int(input("enter a number:"))
    a.append(m)
print(a)

l=len(a)
a.sort()
print(a)
f=0
l=len(a)-1
x=int(input("Enter the number to search :"))
if x in a:   
    while f<=l:
    
        mid=(f+l)//2
        if a[mid]==x:
            print("found at ",mid)
            break
        elif a[mid]>x:
            l=mid-1
        else:
            f=mid + 1
else:
    print("not found")
