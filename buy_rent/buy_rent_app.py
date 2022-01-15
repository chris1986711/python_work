
import streamlit as st
import pandas as pd
import altair as alt

st.header('Buy Or Rent?')

st.write("比較租房或買房的消費部分,裝修利息租金通勤成本。")
st.write("能清楚每個月繳出去的房租或房貸是存起來了，還是給了房東或銀行了。")
st.write("輸入以下條件，我們將用還３０年房貸或租３０年房，分析住幾年以上適合用買的，或先租就可以了。")

st.subheader("國泰房地產指數加權均價2021Q3：")

city = st.selectbox(
    '選擇城市。',
    ['台北市','新北市', '桃園市', '新竹縣市','台中市','台南市','高雄市'])


##
price_dic={'台北市':93.8, '新北市':40.94, '桃園市':27.02, '新竹縣市':27.84,'台中市':27.87,'台南市':24.02,'高雄市':26}

city_price=price_dic[city]

st.write(city,"參考均價：",city_price,"萬每坪。")

st.write('https://www.cathay-red.com.tw/tw/About/House')
#####選擇一個城市dic均價假設面積得出頭期款總價用相同的裝修預算先顯示出均價#####

st.subheader("輸入買的條件：")

down_payment = st.number_input(label = '頭期款(萬)',step=1)

house_price = st.number_input(label = '總價（萬）',step=1)

furnish = st.number_input(label = '裝修款（萬）30年攤提',step=1)

d=int(down_payment)*10000
p=int(house_price)*10000
bf=int(furnish)*10000

prepare_fund=d+bf

st.subheader("買房每月產生的費用：")

interest = st.number_input(label = '年利率%',step=0.1)

commute_buy = st.number_input(label = '買房每天通勤時間（分）',step=1)

loan=p-d
#貸款金額
pm=loan*0.0027777777778
#每月還本３０年
i=int(interest*loan*0.000833)
cb=int(commute_buy)*50
#時薪150計算一個月２０天（分／６０＊１５０＊２０）
pr=int(pm)
#每月還本取整數

buy_comsupmpyion=i+cb
##每個月利息通勤






st.subheader("租房每月產生的費用：")

rent = st.number_input(label = '每月租金',step=1000)

commute_rent = st.number_input(label = '租屋每天通勤時間（分）',step=1)

r=int(rent)#租金取整數
cr=int(commute_rent)*50##時薪150計算一個月２０天（分／６０＊１５０＊２０）

rent_comsumption=r+cr#每個月租金通勤

st.subheader("３０年後的比較：")

#ct = st.number_input(label = '住幾年',step=1)#
compare_time=int(30)
#30年比較
bc=buy_comsupmpyion*compare_time*12
#買房每個月消費＊時間
rc=rent_comsumption*compare_time*12
#租房每個月消費＊時間
bpm=buy_comsupmpyion+pr
#消費加還本
rpm=rent_comsumption
#租房每月銷費
already_pay=d+pr*compare_time*12
#頭期款＋以還的貸款
debt=p-already_pay
#還剩多少沒還
bpm_rpm_diff=bpm-rpm
#租屋每個月多可以運用的錢

##比較城市



if st.button('試算'):
     
    bc1=format(bc,',')
    rc1=format(rc,',')
    prepare_fund1=format(prepare_fund,',')
    bpm1=format(bpm,',')
    rpm1=format(rpm,',')
    bpm_rpm_diff1=format(bpm_rpm_diff,',')
    already_pay1=format(already_pay,',')
    debt1=format(debt,',')
    totalpay=already_pay+bc+bf
    totalpay1=format(totalpay,',')
    st.write("買房消費（利息＋通勤成本）：",bc1,"元")
    st.write("租房消費（租金＋通勤成本）：",rc1,"元")
    st.write("買需準備(自備款裝修款)：",prepare_fund1,"元")
    st.write("買房每月需繳：",bpm1,"元")
    st.write("租房每月需繳：",rpm1,"元")
    st.write("每月差額：",bpm_rpm_diff1,"元")
    st.write("買房（本金部分）:",already_pay1,"元","剩餘房貸:",debt1,"元")
    st.write("買房總共花:",totalpay1,"元")

    

##按３０年還完房貸比較３０年租房

    year=[]
    buy_line=[]
    rent_line=[]
    i=0                 ##畫出數列
    for i in range(0,30):
        by=bf+buy_comsupmpyion*i*12
        ry=rent_comsumption*i*12
        year.append(i)
        buy_line.append(by)
        rent_line.append(ry)
    
    j=0
    y=0                 ##找出交叉點
    for j in range(0,30):
        by=bf+buy_comsupmpyion*j*12
        ry=rent_comsumption*j*12
        if ry > by:
            y=j
            break
    if y==0:
        st.title("租金好便宜啊，租比較划算")
    
            
        
    if y>0:
        st.write("住",y,"年以上適合用買的！！！")
    

    df = pd.DataFrame(
    {
        '年': year,
        '買消費': buy_line,
        '租消費': rent_line
    },
    columns=['年', '買消費', '租消費']
    )

   

    

    df = df.melt('年', var_name='name', value_name='消費')
    

    chart = alt.Chart(df).mark_line().encode(
        x=alt.X('年:N'),
        y=alt.Y('消費:Q'),
        color=alt.Color("name:N")
    ).properties(title="buy or rent?")
    st.altair_chart(chart, use_container_width=True)