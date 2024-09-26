#greatest and smallest number in a array


arr=[]
q=int(input("number :"))
for i in range(q):
    i=int(input())
    arr.append(i)
print(arr)

print(" the higest number is " , max(arr))
print("the lowest number is ", min(arr))

min=arr[0]
max=arr[0]

for i in range(1,len(arr)):
    if arr[i]>max:
        max=arr[i]
    if arr[i]<min:
        min=arr[i]
print(min,max)
