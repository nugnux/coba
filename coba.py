import streamlit as st

st.title('Fisika')
st.header('Komputasi Awan')
st.text('Tulisan')
print('Tadaa...')
st.button("Reset", type="primary")
if st.button("Say hello"):
    st.write("Why hello there")
else:
    st.write("Goodbye")

