#判斷isalpha,isdigit,isalnum,islower,isupper,istitle,isspace組合應用？

last_name = input("last name:",)
frist_name = input("frist name:",)    

if last_name.isalpha()==True and frist_name.isalpha()==True:
   print("姓名:",frist_name,last_name)
elif last_name.isalpha()==False or frist_name.isalpha()==False:
    print("Error")

      
brithday_year = input("西元出生年份:")
brithday_month = input("出生月:")
brithday_day = input("出生日:")

if brithday_year.isdigit()==True and brithday_month.isdigit()==True and brithday_day.isdigit()==True:   #年份（1900～2200)月（1~12)日（1~31)
    print(brithday_year,"/",brithday_month,"/",brithday_day)
else:
    print("error")

add = input("地址（範例：紐約第五大道 24 號）")


target = input("目標（範例：成為史上最強的工程師）")

print("地址:",add)

print("目標:",target)