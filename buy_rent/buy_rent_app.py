
import streamlit as st

import numpy as np
import pandas as pd

st.title('Buy Or Rent?')

st.write("輸入買的條件：")

down_payment = st.number_input(label = '輸入頭期款')

house_price = st.number_input(label = '輸入總價')

furnish = st.number_input(label = '輸入裝修款')

d=int(down_payment)
p=int(house_price)
bf=int(furnish)

prepare_fund=d

st.write("輸入買房每月產生的費用：")

interest = st.number_input(label = '輸入利息')

commute_buy = st.number_input(label = '每月通勤距離km')

principal_repayment = st.number_input(label = '每月還本金')

i=int(interest)
cb=int(commute_buy)*60#每公里平均3塊每月20天
pr=int(principal_repayment)

buy_comsupmpyion=i+cb

st.write("輸入租房每月產生的費用：")

rent = st.number_input(label = '每月租金')

commute_rent = st.number_input(label = '每月通勤距離：')

r=int(rent)
cr=int(commute_rent)*60#同cb

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