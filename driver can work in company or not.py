ms,gen,age=eval(input("enter martial status,gender and age"))
if ms=='m':
    print("can be in the company")
if ms!='m':
    if gen=='m':
        if age>25:
            print("can be")
        else:
            print("cannot be")
    elif gen!='m':
        if age>35:
            print("can be")
        else:
            print("cannot be")
