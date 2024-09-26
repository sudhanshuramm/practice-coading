#prime number up to 100

a=int(input("enter range"))
for i in range(2,a):
    c=1
    for j in range(2,i):
        if i%j==0:
            c=c+1
            break

    if c==1:
        print(i)
   
    
