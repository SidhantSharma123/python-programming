m,yr=eval(input("enter month and year"))
if m==4 | m==6 | m==9| m==11:
    print("no of days are 30")
elif m==2 & yr%4==0:
    print("no of days are 29")
elif m==2 & yr%4!=0:
    print("no of days are 28")
else:
    print("no of days are 31")
