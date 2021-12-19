def checkpal(word):
    b=list (word)  
    c=list(reversed(word))
    if b == c:
        return True
    else:
        return False



a=input("check palindrome:")
print(checkpal(a))