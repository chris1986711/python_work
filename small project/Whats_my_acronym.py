def acr(w):
    w1=str(w)
    wlist=w1.split()
    x=len(wlist)
    i=0
    ans=[]
    while i <= x-1:
        l1=wlist[i]
        l2=list(l1)
        l3=l2[0].upper()
        ans.append(l3)
        i=i+1
    stra="".join(ans)
    return stra

word= input("輸入英文字串:")


print("字串縮寫:",acr(word))    



#strlwr(sStr1)轉換大小寫範例(upper.(),lower())
#sStr1 = 'JCstrlwr'
#sStr1 = sStr1.upper()
#sStr1 = sStr1.lower()
#print (sStr1)

#split() 預設以空白字元來切割，並回傳包含分拆後各個字串的串列（list），回傳的資料型態是串列。

#>>>print('You work very hard!'.split())
#['You', 'work', 'very', 'hard!']