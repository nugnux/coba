import streamlit as st
import random
import matplotlib.pyplot as plt


st.title("Fisika Komputasi Awan")
st.title("Nugroho Adi Pramono :sunglasses:")
x = []
y = []
color = []
size = []
x.append(0)
y.append(0)
if st.button("Data"):
    for i in range(10):
        x.append(random.random() - .5)
        y.append(random.random() - .5)
        c.append(random.random() )
        s.append(random.random() )
    
fig, ax = plt.subplots(figsize=(16, 8))
ax.plot(x, y, c=color, s=size, alpha=0.5) 

ax.set_ylabel("y")
ax.set_xlabel("x")
ax.tick_params(axis='y', labelsize=20)
ax.set_xticklabels(ax.get_xticklabels(), rotation=30, ha='right')
ax.tick_params(axis='x', labelsize=15)
ax.set_title('Data Acak yang berubah setiap tombol ditekan')
st.pyplot(fig)
