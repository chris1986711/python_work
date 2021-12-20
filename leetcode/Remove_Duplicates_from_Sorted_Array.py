nums=[1,1,2,2,3,3,4,4,5,5]
def rd(n:list):
    k=len(n)
    i=0
    j=0
    n2=[None]*k
    while i <=k-1:
        if n[i]==n[k-1]:
            n2[j]=n[i]
            break
        elif n[i]==n[i+1]:
            i=i+1
        elif n[i]!=[i+1]:
            n2[j]=n[i]
            i=i+1
            j=j+1
    return n2

p=rd(nums)
print(p)
        
