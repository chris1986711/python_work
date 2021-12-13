#判斷isalpha,isdigit,isalnum,islower,isupper,istitle,isspace組合應用？

last_name = input("last name:",)
first_name = input("frist name:",)    

if last_name.isalpha() and first_name.isalpha():
   print("姓名:",first_name,last_name)
elif not last_name.isalpha() or not first_name.isalpha():
    print("Error")

      
brithday_year = input("西元出生年份:")
brithday_month = input("出生月:")
brithday_day = input("出生日:")

if brithday_year.isdigit() and brithday_month.isdigit() and brithday_day.isdigit():   #年份（1900～2200)月（1~12)日（1~31)
    print(brithday_year,"/",brithday_month,"/",brithday_day)
else:
    raise ValueError("輸錯啦！請輸入正確的出生年月日格式")

add = input("地址（範例：紐約第五大道 24 號）")


target = input("目標（範例：成為的程序猿）")

print("地址:",add)

print("目標:",target)