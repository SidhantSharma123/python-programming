l1=[10,20,10,30,50,20,10]
l2=[]
for item in l1:
    if item not in l2:
        l2.append(item)
print(l2)
