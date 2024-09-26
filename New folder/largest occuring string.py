""" print the largest occuring string in a string"""

a="this is a man and this is the hero this"

l=a.split()
higher=0
high=0
for i in l:
    occ=0
    for j in l:
        if i==j:
            occ=occ+1

    if occ>high:
        high=occ
        higher=i
print(higher)
    
    
            
        
        
