PR,NR,MT=eval(input("enter PR,NR and meter type"))
UC=NR-PR
if MT=="D":
    RPU=5.50
elif MT=="C":
    RPU=7.50
bill=UC*RPU
print("bill is",bill)
