import streamlit as st
import pandas as pd
import numpy as np

st.title("Unegui.mn")
st.markdown("Та доорх 4 шүүлтүүрийг сонгоно уу.")

df = pd.read_excel("excel.xlsx")


col6, col7 = st.columns(2)
regular_search_term =sorted(df.car_brand.unique().tolist())
choices = col6.selectbox(" ",regular_search_term)

df2 = df[df.car_brand.isin([choices])]
col6.markdown("Машины марк")

regular_search_term2 = sorted(df2.car_name.unique().tolist())
choices2 = col7.selectbox(" ",regular_search_term2)

df3 = df2[df2.car_name.isin([choices2])]
col7.markdown("Машины нэр")

df3["manufactured_year"] = pd.to_numeric(df3["manufactured_year"])
df3["imported_year"] = pd.to_numeric(df3["imported_year"])

col4, col5 = st.columns(2)
regular_search_term3 =sorted(df3.manufactured_year.unique().tolist())
choices3 = col4.selectbox(" ",regular_search_term3)

df4 = df3[df3.manufactured_year.isin([choices3])]
col4.markdown("Машины үйлдвэрлэсэн он")

regular_search_term4 =sorted(df4.imported_year.unique().tolist())
choices4 = col5.selectbox(" ",regular_search_term4)

df5 = df4[df4.imported_year.isin([choices4])]
col5.markdown("Машины орж ирсэн он")

df5["price"] = df5["price"].astype(float)
df5["viewed_by"] = pd.to_numeric(df5["viewed_by"])
df5["mileage"] = pd.to_numeric(df5["mileage"])
df5["doors"] = pd.to_numeric(df5["doors"])
df5["motor_size"] = pd.to_numeric(df5["motor_size"])


def btn_click():
    st.markdown("<h4 style='text-align: center; color: black;'>Ерөнхий мэдээлэл</h1>", unsafe_allow_html=True)
    
    col8, col9 = st.columns(2)
    uni = df5['des']. nunique()
    
    with col8.container():
        col8.info(':car: Нийт зар тавигдсан машины тоо')
    
    with col9.container():
        col9.info(uni)
    
    col1, col2, col3 = st.columns(3)
    numbers_avg = "{:,}".format(df5["price"].mean())
    numbers_min = "{:,}".format(df5["price"].min())
    numbers_max = "{:,}".format(df5["price"].max())
    
    with col1.container():
       col1.info(':moneybag: Дундаж үнэ')
       col1.info(numbers_avg)
       
    with col2.container():
       col2.info(':small_red_triangle_down: Min үнэ')
       col2.info(numbers_min)
    
    with col3.container():
        col3.info(':small_red_triangle: Max үнэ')
        col3.info(numbers_max)
    
    st.write(df5)

button = st.button(":globe_with_meridians: Шалгах",on_click=btn_click)

