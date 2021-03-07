str1=str(input("enter any string"))
str2=str(input("enter the string you want to insert in the middle"))
print(str1[0:len(str1)//2]+str2+str1[len(str1)//2:])
