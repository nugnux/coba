import streamlit as st
import random
import matplotlib.pyplot as plt


st.title("Fisika Komputasi Awan")
st.title("Nugroho Adi Pramono :sunglasses:")
x = []
y = []
x.append(0)
y.append(0)
if st.button("Data"):
    x.append(random.random() - .5)
    y.append(random.random() - .5)
    
fig, ax = plt.subplots(figsize=(16, 8))
ax.plot(x, y, label='Plot titik acak', color='g') 

ax.set_ylabel("")
ax.set_xlabel("x")
ax.tick_params(axis='y', labelsize=20)
ax.set_xticklabels(ax.get_xticklabels(), rotation=30, ha='right')
ax.tick_params(axis='x', labelsize=15)
st.pyplot(fig)
