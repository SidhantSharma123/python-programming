x=str(input("enter the string"))
if len(x)<2:
    print("0")
else:
    print(x[0:2]+x[len(x):len(x)-3:-1])

