d={"Ram":(80,30,30),"Amit":(60,70,90),"Mohan":(50,40,60)}
s=list(d.values())
v=list(d.keys())
for x in s:
    s.sort(key=lambda t:tuple(t))

print(s)
