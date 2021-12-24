####買房####
###一次性部分###

down_payment=input("頭期款：")
house_price=input("總價：")
furnish=input("裝修款：")
d=int(down_payment)
p=int(house_price)
bf=int(furnish)

prepare_fund=d

###每個月產生###

interest=input("利息：")
commute_buy=input("每月通勤距離km:")
principal_repayment=input("每月還本金：")
i=int(interest)
cb=int(commute_buy)*60#每公里平均3塊每月20天
pr=int(principal_repayment)

buy_comsupmpyion=i+cb

####租房####
###每個月產生###

rent=input("每月租金:")
commute_rent=input("每月通勤距離：")

r=int(rent)
cr=int(commute_rent)*60#同cb

rent_comsumption=r+cr

####比較####
ct=input("住幾年")
compare_time=int(ct)
bc=buy_comsupmpyion*compare_time*12
rc=rent_comsumption*compare_time*12
bpm=buy_comsupmpyion+pr
rpm=rent_comsumption
already_pay=d+pr*compare_time*12
debt=p-already_pay


print("買房消費:",bc,"租房消費:",rc)
if bc > rc:
    print("租比較好")
else:
    print("買比較好,需準備",prepare_fund)
print("買房每月需繳：",bpm,"租房每月需繳：",rpm)
print("資產:",already_pay,"剩餘房貸:",debt)