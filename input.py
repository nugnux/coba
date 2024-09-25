import streamlit as st

x = st.number_input("Masukkan suhu")
sx = st.text_input("Satuan", "C")
st.write("Anda menginput suhu ", x," dengan satuan ", sx )
sy = st.text_input("konversi ke", "C")

st.write("Hasil konversi dari ",x,sx," adalah ...", sy )
