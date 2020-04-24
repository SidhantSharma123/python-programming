str1=str(input("enter any string"))
l1=list(str1)
l2=[]
for x in l1:
    if x not in l2:
        l2.append(x)
s="".join(l2)
print(s)
