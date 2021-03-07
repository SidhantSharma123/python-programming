l=['p','q']
n=int(input("enter the value of n"))
li=[]
for i in range(1,n+1):
    x=list(map(lambda s: s+str(i),l))
    li.extend(x)
print(li)
