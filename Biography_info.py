#判斷isalpha,isdigit,isalnum,islower,isupper,istitle,isspace組合應用？

name = input("姓名（範例：John Doe）")
    
if name.isalpha()==True:
   print("姓名:",name)
elif name.isalpha()==False:
    print("Error")

      
brithday = input("範例：1954/1/1")

if brithday.isdigit()==True:
    print(brithday)
else:
    print("error")
add = input("地址（範例：紐約第五大道 24 號）")

target = input("目標（範例：成為史上最強的工程師）")



print("生日:",brithday)

print("地址:",add)

print("目標:",target)