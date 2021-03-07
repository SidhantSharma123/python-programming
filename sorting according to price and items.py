l=[('item','12.20'),('item','15.10'),('item','124.5')]
for x in l:
        x[1]=float(x[1])
        
        l.sort(key=lambda t:t[-1])
print(l)
