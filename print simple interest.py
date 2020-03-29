def si(p,t,r=0.02):
    s=p*r*t/100
    return s
a=eval(input("enter principle"))
b=eval(input("enter time"))
d=si(a,b)
print("simple interest is",d)
    
