# -*- coding: utf-8 -*-
"""AppPOC.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1d2612uzSLqyKxzZhhifEtR-Zb6Kj7K61
"""

import streamlit as st
st.title('Hello, Streamlit!')
st.write("Welcome to your first Streamlit app!")
name = st.text_input("Enter your name:")
if st.button('Say Hello'):
    st.write(f"Hello, {name}!")
else:
    st.write("Please click the button to say hello!")