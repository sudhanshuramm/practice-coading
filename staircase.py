def staircase(n):
    # Write your code here
    for i in range(n,0):
        for j in range(n):
            if i>=j:
                print("",end=" ")
            else:
                print("#",end="")
        print("/n")



a=int(input())
staircase(a)
