basic=eval(input("enter basic salary"))
if basic>5000:
    bonus=0.1*basic
else:
    bonus=0.05*basic
totsal=bonus+basic
print("total salary is",totsal)
