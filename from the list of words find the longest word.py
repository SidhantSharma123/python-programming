l=[]
n=int(input("enter the no of words"))
for x in range(0,n):
    lis=str(input())
    l.append(lis)
l.sort(key=lambda s:len(s),reverse=True)
print(l[0])
