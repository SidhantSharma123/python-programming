n=eval(input("enter any no"))
sum=0
for x in range(n,1):
    r=x%10
    sum=sum+r
    x=x/10
print("sum of digit is",sum)
