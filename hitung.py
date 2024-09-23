import streamlit as st

x = st.number_input("Masukkan angka")
sx = st.selectbox("Satuan", ("C", "F", "R","K"), key='sx')
st.write ("Anda memasukkan", x,' ',sx)
sy = st.selectbox("Dikonversi ke", ("C", "F", "R","K"), key='sy')
y = 0
if (sx == 'C'):
  if(sy == 'C'):
    y = x
  elif(sy == 'F'):
    pass
st.write (x,' ',sx, ' = ',y, sy)



