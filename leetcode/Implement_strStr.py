a="a"
b=""
a_list=list(a)
b_list=list(b)
k=len(a_list)-1
l=len(b_list)-1
i=0
j=0
if b in a:
    print(True)
    while i<=k:
        if a_list[i]==b_list[0]:
            break
        elif a_list!=b_list[0]:
            i=i+1
    print(i)
else:
    print(-1)
    print(False)

    


