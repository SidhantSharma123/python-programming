def perno(n):
    sum=0
    for i in range(1,n//2+1):
        if n%i==0:
            sum=sum+i
    if n==sum:
        return "it is a perfect no"
    else:
        return "it is not a perfect no"
a=int(input("enter any no"))
c=perno(a)
print(c)
