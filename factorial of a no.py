def fact(x):
    fac=1
    for i in range(1,x+1):
        fac=fac*i
    return fac
a=int(input("enter any no"))
c=fact(a)
print(c)
