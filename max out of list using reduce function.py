import functools
f=lambda a,b:a if a>b else b
print(functools.reduce(f,[5,4,9,2,1,6]))
