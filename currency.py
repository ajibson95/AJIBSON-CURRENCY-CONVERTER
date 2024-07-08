import streamlit as st
from PIL import Image
import numpy as np

st.title("My Currency Converter App")

img = Image.open("currency.jpeg")
st.image(img)

currency = ["NGN", "USD" , "JPY", "CAD", "GBP"]

conv = [1, 0.00065, 0.10, 0.0008, 0.00051]

def curr_converter(amt, curr_f, curr_t):

    ind_f = currency.index(curr_f)
    ind_t = currency.index(curr_t)

    rate_f = conv[ind_f]
    rate_t = conv[ind_t]

    value = amt * (rate_t/rate_f)
    value = round(value,2)
    return value



amt = st.number_input("Amount")
curr_f = st.selectbox("From",currency)
curr_t = st.selectbox("To", currency)

if st.button("Convert"):
    val = curr_converter(amt, curr_f, curr_t)
    st.success(val)