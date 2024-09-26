#find second largest and second smallest number in list

def slarger(a):
    lar=float("-inf")
    slar=lar
    for i in a:
        if i>lar:
            slar=lar
            lar=i
        elif i>slar and i<lar:
            slar=i
    return slar

def ssmaller(a):
    lar=float("+inf")
    slar=lar
    for i in a:
        if i<lar:
            slar=lar
            lar=i
        elif i<slar and i>lar:
            slar=i
    return slar

#a=[]
num=int(input("number :"))
a=list(map(int,input().split()))
"""for i in range(num):
    a.append(int(input( )))"""
print(slarger(a))
print(ssmaller(a))
    
