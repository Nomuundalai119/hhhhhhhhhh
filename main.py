import streamlit as st
import pandas as pd


st.title("Unegui.mn")
st.markdown("зориулалттай хийгдэв.")

df = pd.read_excel("excel.xlsx")


st.markdown("Машины марк сонгоно уу.")
regular_search_term =df.car_brand.unique().tolist()
choices = st.selectbox(" ",regular_search_term)

df2 = df[df.car_brand.isin([choices])]

st.markdown("Машины нэр сонгоно уу.")
regular_search_term2 =df2.car_name.unique().tolist()
choices2 = st.selectbox(" ",regular_search_term2)

df3 = df2[df2.car_name.isin([choices2])]

st.markdown("Машины үйлдвэрлэсэн он сонгоно уу.")
regular_search_term3 =df3.manufactured_year.unique().tolist()
choices3 = st.selectbox(" ",regular_search_term3)

df4 = df3[df3.manufactured_year.isin([choices3])]

st.markdown("Машины орж ирсэн он сонгоно уу.")
regular_search_term4 =df4.imported_year.unique().tolist()
choices4 = st.selectbox(" ",regular_search_term4)

df5 = df4[df4.imported_year.isin([choices4])]

st.write(df4)

