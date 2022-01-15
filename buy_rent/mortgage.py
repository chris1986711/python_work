  
    

###本金平均攤還法####

principal=input("本金多少萬元：")
p=int(principal)*10000
rate_year=input("年利率幾％：")
ry=float(rate_year)*0.01
rm=ry/12#月息＝年息/12
loan_year=input("貸款年數：")
ly=int(loan_year)
lm=ly*12#貸款月數
repayment_principal_month=p/lm
#利息表
i=0
interest_list=[]
payment_month=[]
while i <= lm:
    im=p*(lm-i)//lm*rm
    im1=round(im)
    im2=round(im1+repayment_principal_month)
    interest_list.append(im1)
    payment_month.append(im2)
    i=i+1
total_interest=sum(interest_list)
total_payment=sum(payment_month)
average_payment=round(total_payment/lm)
##每月本息還款##

print("總還款：",total_payment,"總利息：",total_interest,"平均每月還：",average_payment)
