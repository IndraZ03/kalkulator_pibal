import streamlit as st
import math
import numpy as np
st.title('Kalkulator Pibal')

p1 = st.number_input('1. Pembacaan ke :')
a1 = float(st.number_input('1. Masukkan nilai azimuth: '))
en1 = float(st.number_input("1. Masukkan nilai elevasi : "))

p2 = st.number_input('2. Pembacaan ke :')
a2 = float(st.number_input('2. Masukkan nilai azimuth: '))
en2 = float(st.number_input("2. Masukkan nilai elevasi : "))


en1 = math.radians(en1)
en2 = math.radians(en2)

if st.button("Hitung Pembacaan"):
    d1 = ((2*p1-1)*250*(1/np.tan(en1)))/202.67
    d2 = ((2*p2-1)*250*(1/np.tan(en2)))/202.67
    st.write(f'D1 = {d1}')
    st.write(f'D2 = {d2}')
    a1 = math.radians(a1)
    a2 = math.radians(a2)
    
    y1 = d1*np.cos(a1)
    y2 = d2*np.cos(a2)

    x1 = d1*np.sin(a1)
    x2 = d2*np.sin(a2)
    deltay = y1-y2
    
    deltax = x1-x2
    st.write(f'ΔX = {deltax}')
    st.write(f'ΔY = {deltay}')
    ff = math.sqrt(deltax**2 + deltay**2) * 2
    
    alfa = np.arctan(deltay/deltax)
    alfa = math.degrees(alfa)
    
    if deltay < 0 and deltax < 0:
       dd = 270 - alfa
    elif deltay <0 and deltax > 0:
        dd = 90 + alfa
    elif deltay > 0 and deltax < 0:
        dd = 270 + alfa
    else :
        dd = 90-alfa    
   
    st.write(f'alfa : {alfa}')
    st.write(f'ff(kec.angin): {ff}')
    st.write(f'dd(arah angin): {dd}')
