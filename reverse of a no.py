n=eval(input("enter any no"))
sum=0
while(n>0):
    r=n%10
    sum=sum*10+r
    n=n//10
print("reverse of the no is ",sum)
