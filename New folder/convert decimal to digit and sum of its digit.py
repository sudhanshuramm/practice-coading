#convert decimal to digit and sum of its digit

def sumdigit(num):
    a=0
    while num !=0:
        a=a+num%2
        
        
        num=num//2
    return a
c=int(input("Enter a number:"))
summ=sumdigit(c)
print(summ)

