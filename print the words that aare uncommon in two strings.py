str1=str(input("enter first string"))
str2=str(input("enter second string"))
l1=str1.split(" ")
l2=str2.split(" ")
l3=[]
for x in l1:
    if x not in l2:
        l3.append(x)
print(l3)
