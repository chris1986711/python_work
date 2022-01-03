
import streamlit as st

st.title('Buy Or Rent?')
st.write("比較租房或買房的消費部分,利息租金通勤成本。")
st.write("能清楚每個月繳出去的房租或房貸是存起來了，還是給了房東或銀行了。")
st.write("也能評估要準備多少頭期款，加入有房一族（房奴？中產？）喔！")
st.write("輸入買的條件：")

down_payment = st.number_input(label = '頭期款(萬)')

house_price = st.number_input(label = '總價（萬）')

furnish = st.number_input(label = '裝修款（萬）20年攤提')

d=int(down_payment)*10000
p=int(house_price)*10000
bf=int(furnish)*10000

prepare_fund=d+bf

st.write("買房每月產生的費用：")

interest = st.number_input(label = '年利率')

commute_buy = st.number_input(label = '買房每天通勤時間（分）')

pm = st.number_input(label = '每月還本')

loan=p-d
i=int(interest*loan*0.000833)
cb=int(commute_buy)*50#時薪150計算一個月２０天（分／６０＊１５０＊２０）
pr=int(pm)#先用輸入的
fm=bf*0.004167#裝修每個月攤提

buy_comsupmpyion=i+cb+fm

st.write("租房每月產生的費用：")

rent = st.number_input(label = '每月租金')

commute_rent = st.number_input(label = '租屋每天通勤時間（分）')

r=int(rent)
cr=int(commute_rent)*50##時薪150計算一個月２０天（分／６０＊１５０＊２０）

rent_comsumption=r+cr

st.write("比較")

ct = st.number_input(label = '住幾年：')
compare_time=int(ct)
bc=buy_comsupmpyion*compare_time*12
rc=rent_comsumption*compare_time*12
bpm=buy_comsupmpyion+pr
rpm=rent_comsumption
already_pay=d+pr*compare_time*12
debt=p-already_pay

st.write("買房消費:",bc,"租房消費:",rc)
st.write("買需準備",prepare_fund)
st.write("買房每月需繳：",bpm,"租房每月需繳：",rpm)
st.write("資產:",already_pay,"剩餘房貸:",debt)

if bc>rc:
    st.title("先租房吧！！！")
if rc>bc:   
    st.title("準備買房吧！！！")