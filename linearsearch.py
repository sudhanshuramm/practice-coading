#find target number in araray
c=0
a=[2,4,65,78,9,63,4]
print(a)
num=int(input())
for i in range(len(a)):
    if a[i]==num:
        print("found AT ",i)
        c=1
if c!=1:
    print("not found")
    
    

