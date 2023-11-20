import streamlit as st

st.title("CALCULATOR APP")
col1, col2, col3 = st.columns(3)

def add(a,b):
    c = a+b
    return c

def sub(a,b):
    c = a-b
    return c

def Mul(a,b):
    c = a*b
    return c

x = st.number_input("input your first number")
y = st.number_input("input your second number")

with col1:
    if st.button("add"):
        st.write(add(x,y))

with col2:
    if st.button("subtract"):
        st.write(sub(x,y))

with col3:
    if st.button("multiply"):
         st.write(Mul(x,y))