s=str(input("enter any string"))
s1=''
for x in range(len(s)):
    if x%2!=0:
        s1=s1+s[x]
print(s1)

