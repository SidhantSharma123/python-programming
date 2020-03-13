n=eval(input("enter any no"))
sum=0
temp=n
while(n>0):
    r=n%10
    sum=sum+(r**3)
    n=n//10
if sum==temp:
    print("it is an armstrong no")
else:
    print("it is not an armstrong no")
