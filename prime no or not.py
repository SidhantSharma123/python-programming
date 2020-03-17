n=eval(input("enter any no"))
i=2
flag=0
while(i<=n/2):
    if n%i==0:
        flag=1
        break
    i=i+1
if flag==0:
    print("prime no")
else:
    print("not a prime no")
