l=[]
l1=[]
n=eval(input("enter no of elements in list"))
for x in range(0,n):
    lis=str(input())
    l.append(lis)
for i in l:
    if i[0]==i[-1]:
        l1.append(i)
    else:
        pass
print(l1)
