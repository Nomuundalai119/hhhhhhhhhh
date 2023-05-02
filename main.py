import streamlit as st
import pandas as pd
import numpy as np

st.title("Unegui.mn")
st.markdown("зориулалттай хийгдэв.")

df = pd.read_excel("excel.xlsx")


col6, col7 = st.columns(2)
regular_search_term =df.car_brand.unique().tolist()
choices = col6.selectbox(" ",regular_search_term)

df2 = df[df.car_brand.isin([choices])]
col6.markdown("Машины марк сонгоно уу.")

regular_search_term2 =df2.car_name.unique().tolist()
choices2 = col7.selectbox(" ",regular_search_term2)



df3 = df2[df2.car_name.isin([choices2])]
col7.markdown("Машины нэр сонгоно уу.")


col4, col5 = st.columns(2)
regular_search_term3 =df3.manufactured_year.unique().tolist()
choices3 = col4.selectbox(" ",regular_search_term3)

df4 = df3[df3.manufactured_year.isin([choices3])]
col4.markdown("Машины үйлдвэрлэсэн он сонгоно уу.")

regular_search_term4 =df4.imported_year.unique().tolist()
choices4 = col5.selectbox(" ",regular_search_term4)

df5 = df4[df4.imported_year.isin([choices4])]
col5.markdown("Машины орж ирсэн он сонгоно уу.")

df5["price"] = pd.to_numeric(df5["price"])
df5["viewed_by"] = pd.to_numeric(df5["viewed_by"])
df5["mileage"] = pd.to_numeric(df5["mileage"])
df5["doors"] = pd.to_numeric(df5["doors"])
df5["motor_size"] = pd.to_numeric(df5["motor_size"])



col1, col2, col3 = st.columns(3)

average_price = df5["price"].mean()
min_price = df5["price"].min()
max_price = df5["price"].max()

with col1.container():
  col1.info(':red_car: Дундаж үнэ')
  col1.info(average_price)

with col2.container():
  col2.info(':red_car: Min үнэ')
  col2.info(min_price)

with col3.container():
  col3.info(':red_car: Max үнэ')
  col3.info(max_price)

##n = len(pd.unique(df5['des']))
##st.markdown("Нийт машины тоо :", n)

st.write(df4)
