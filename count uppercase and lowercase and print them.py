def upplow(s):
    c1=0
    c2=0
    if s.islower()==True:
        print(s.islower())
        c1=c1+1
    else:
        print(s.isupper())
        c2=c2+1
    return c1,c2
a=str(input("enter any string"))
c=upplow(a)
print(c)
