l=[]
n=int(input("enter the no of variables in list"))
for x in range(0,n):
    lis=eval(input(""))
    l.append(lis)
l.remove(max(l))
n=max(l)
print(n)
