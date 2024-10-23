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
color.append((0.,.7,0.))
size.append(73)
if st.button("Data"):
    for i in range(10):
        x0 = random.random() - .5
        y0 = random.random() - .5
        if ((x0**2+y0**2)>1.):
            x0 = x0/2.
            y0 = y0/2.
            
        x.append(x0)
        y.append(y0)
        color.append((random.random(),random.random(),random.random()))
        size.append(1713*random.random() )
    
fig, ax = plt.subplots(figsize=(16, 8))
ax.scatter(x, y, c=color, s=size, alpha=0.5) 

ax.set_ylabel("y")
ax.set_xlabel("x")
ax.tick_params(axis='y', labelsize=20)
ax.set_xticklabels(ax.get_xticklabels(), rotation=30, ha='right')
ax.tick_params(axis='x', labelsize=15)
ax.set_title('Data Acak yang berubah setiap tombol ditekan')
ax.set_xlim([-1, 1])
ax.set_ylim([-1, 1])
st.pyplot(fig)
