l1=[]
for x in range(1,6):
    lis=eval(input())
    l1.append(lis)
f=lambda c:(float(9)/5)*c+32
l=list(map(f,l1))
print(l)
