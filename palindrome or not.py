n=eval(input("enter any no"))
sum=0
temp=n
while(n>0):
    r=n%10
    sum=sum*10+r
    n=n//10
if(sum==temp):
    print("it is a palindrome no")
else:
    print("it is not a palindrome no")
