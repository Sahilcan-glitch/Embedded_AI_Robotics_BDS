import streamlit as st

st.title("Week 3 – Hello Streamlit 👋")
st.write("If you can see this in your browser, Streamlit is working!")

name = st.text_input("Your name:")
if name:
    st.success(f"Nice to meet you, {name}!")
