count=0
def peli(a):
    global count
    b=a
    x=len(str(b))
    c=0
    while a !=0:
        z=a%10
        c=(z**x)+c
        a=a//10
    if c==b:
        print(c)
        count=count+1
    

num=int(input("enter limit:"))
i=1
while i>0:
    
    if count==num:
        break
    else:
        peli(i)
    i=i+1
