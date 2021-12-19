
    

###本金平均攤還法####

principal=input("本金多少萬元：")
p=int(principal)*10000
rate_year=input("年利率幾％：")
ry=float(rate_year)*0.01
rm=ry/12#月息＝年息/12
loan_year=input("貸款年數：")
ly=int(loan_year)
lm=ly*12#貸款月數
repayment_principal_month=p//lm
print(p,ry,rm,ly,lm)
i=0
interest_list=[]
while i <= lm:
    im=p*(lm-i)//lm*rm
    im1=int(im)
    interest_list.append(im1)
    i=i+1
print(interest_list)
##def 每月利息into list##

