n=eval(input("enter the no that should be checked"))
flag=0
for x in range(2,n):
    if n%x==0:
        flag=1
if(flag==0):
    print("it is a prime no")
else:
    print("it is not a prime no")
