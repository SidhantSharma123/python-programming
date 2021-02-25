def printext(s):
    l=s.split(".")
    return l[-1]
str1=str(input("enter any file name"))
c=printext(str1)
print("."+c)
