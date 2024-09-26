#consecutive armstrong number
num=int(input("Enter a number :"))




a=int(input("enter a number :"))
b=a
x=len(str(b))
c=0
while a !=0:
    z=a%10
    c=(z**x)+c
    a=a//10
if c==b:
    print("armstrong")
else :
    print("not armstrong")
    
