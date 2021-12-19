
x=2

while x>1:
    inputnum=int(input("輸入你猜的數字："))
    ans=89
    if inputnum==ans:
        print("正確")
        x-=1
    elif inputnum>ans:
        print("比答案大")
    elif inputnum<ans:
        print("比答案小")