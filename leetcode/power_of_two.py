def power(b:int):
    j=0
    while 2**j<=b:
        if 2**j==b:
            return True
        elif 2**j<b:
            j+=1
    return False


n=input()
n=int(n)
print(power(n))
