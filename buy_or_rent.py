####買房####
###一次性部分###

down_payment=input("頭期款：")
house_price=input("總價：")
furnish=input("裝修款：")
d=int(down_payment)
p=int(house_price)
f=int(furnish)

sum_buy_once=d+p+f
###每個月產生###

interest=input("利息：")
commute_buy=input("每月通勤距離km:")
principal_repayment=input("每月還本金：")
i=int(interest)
cb=int(commute_buy)*3#每公里平均3塊
pr=int(principal_repayment)

sum_buy_monthly=i+cb+pr

####租房####
###每個月產生###

rent=input("每月租金:")
commute_rent=input("每月通勤距離：")

r=int(rent)
cr=int(commute_rent)*3#每公里平均3塊

sum_rent_monthly=r+cr

####比較####

compare_time=input("打算住幾年:")
average_time_year=9

sum_buy_avg=sum_buy_once + sum_buy_monthly*average_time_year*12
sum_rent_avg=sum_rent_monthly*average_time_year*12

if sum_buy_avg > sum_rent_avg:
    print("買>租")
else:
    print("租>買")