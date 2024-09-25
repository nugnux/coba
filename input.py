import streamlit as st

x = st.number_input("Masukkan angka")
st.write("Anda menginput angka ", x)
st.write("Kuadratnya ", x*x)
