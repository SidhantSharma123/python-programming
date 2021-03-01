p,m,c=eval(input("enter marks of physics ,maths and chemistry"))
per=p+m+c/3
if per>=75:
    print("distinction")
elif per>=60 & per<75:
    print("first division")
elif per>=50 & per<60:
    print("second division")
elif per<50:
    print("fail")
    
