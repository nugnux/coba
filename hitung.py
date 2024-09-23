import streamlit as st

x = st.number_input("Masukkan angka")
st.write("Anda memasukkan angka", x)
sx = st.text_input("Movie title", "Life of Brian")
st.write (sx)

