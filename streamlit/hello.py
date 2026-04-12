import streamlit as st 
st.title("Hello world of streamlit")
st.subheader("Brewed with streamlit")
st.text("Welcome to first interactive app")
st.write("choose your favourite variety of chai")
select = st.selectbox("Your favourite chai : ", ["masala chai", "lemon tea", "adrak chai"])
st.write(f" Your Choise {select}. Excellecebt chai")

st.success("Your chai has been brewed")