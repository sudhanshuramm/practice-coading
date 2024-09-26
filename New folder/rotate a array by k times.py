#rotate a array in k times
""" ex - a=[1,2,4,5,7] and k=3
output is -  a=[4,5,7,1,2]
"""
a=[1,2,3,4,5,6,7]
k=3

l=len(a)
s=l-k
print(s)
add= a[s:l]+a[:s]
print(add)
