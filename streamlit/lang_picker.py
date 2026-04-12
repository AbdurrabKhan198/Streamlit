import streamlit as st

st.title("Welcome to the language picker app ")
st.header("You have to choose your favourite language")

choose = st.selectbox("Your favorite language : ", ["python ", "java"])
st.write("hii")
st.success(f" your fav programming language is {choose} : Excellent choise")