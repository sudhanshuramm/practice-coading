#consecutive prime numbers


n=int(input("Enter a number : "))
x=0
c=2
while n>0:
    j=2
    num=0
    while j<c:
        if c%j==0:
            
            num=num+1
            break
        j=j+1
    if num==0:
        x=x+1
        print(c)
    if x==n:
        break
    c=c+1
        
