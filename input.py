import streamlit as st

x = st.number_input("Masukkan angka")
sx = st.text_input("Satuan", "C")
st.write("Anda menginput suhu ", x," dengan satuan ", sx )
st.write("Kuadratnya ", x*x)
