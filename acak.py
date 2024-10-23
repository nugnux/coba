import streamlit as st
import random
import matplotlib.pyplot as plt


st.title("Fisika Komputasi Awan")
st.title("Nugroho Adi Pramono :sunglasses:")
x = []
y = []
if st.button("Data"):
    x.append(random.random() - .5)
    y.append(random.random() - .5)
fig, ax = plt.subplots(figsize=(16, 8))
ax.plot(x, y, label='cos(x)', color='g') 
