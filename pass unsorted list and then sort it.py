def sor(l):
    l.sort()
    return l
l1=[]
for x in range(0,5):
    lis=eval(input())
    l1.append(lis)
c=sor(l1)
print("sorted list is",c)
