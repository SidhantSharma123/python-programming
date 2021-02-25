l=[1,2,3,4,5]
fact=1
s=[fact*i for x in l for i in range(1,l[x]+1)]
print(s)
