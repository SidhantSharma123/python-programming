def sumdigits(x):
    sum=0
    while x>0:
        r=x%10
        sum=sum+r
        x=x//10
    return sum
a=int(input("enter any no"))
c=sumdigits(a)
print(c)
