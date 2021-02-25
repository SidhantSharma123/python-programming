def strpalindrome(s):
    str1=s[::-1]
    if str1==s:
        return "string is palindrome"
    else:
        return "string is not palindrome"
a=str(input("enter any string"))
c=strpalindrome(a)
print(c)
