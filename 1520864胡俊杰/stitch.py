def reverse(s):
    if s=="":
        return ""
    else :
        return reverse(s[1:])+s[0]
    
