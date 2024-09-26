#correct file name problem
string=input()
a=string.split(",")
c=0
for i in a:
    temp=i.split("_")
    if temp[0]=="file" or temp[0]=="File":
        if temp[1].isdigit():
            c=c+1
print(c)
        
