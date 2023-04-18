import streamlit as st

st.write('Enter Three Numbers')

a=st.number_input('Enter 1st No.')
b=st.number_input('Enter 2nd No.')
c=st.number_input('Enter 3rd No.')

st.write(max(a,b,c))
