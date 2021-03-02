l=[]
n=eval(input("enter no of elements in list"))
for x in range(0,n):
    lis=str(input())
    l.append(lis)
l.sort(key=lambda s:s.lower())
print(l)
