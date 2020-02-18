CP,SP=eval(input("enter cost price and selling price"))
if CP>SP:
    loss=CP-SP
    print("loss is",loss)
else:
    loss=SP-CP
    print("loss is",loss)
