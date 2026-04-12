import streamlit as st

st.title("Chai Maker App")

if st.button("Make chai"):
    st.success("Your chai is being brewed")

add_masala = st.checkbox("Add Masala")

if add_masala:
    st.write("masala added to your chai")

tea_type = st.radio("Pick your chai base : ", ["Milk","Water", "Honey"])

st.write(f"Selected base {tea_type}")

flavour = st.selectbox("Choose flavour : ", ["Adrak", "Kesar"])
st.write(f"Selected flavour  {flavour}")

sugar = st.slider("Sugar level (spoon)", 0, 2, 5)
st.write(f"Selected sugar level   {sugar}")

cups = st.number_input("How many cups", min_value=1, max_value=10, step=1)

st.write(f" {cups} cups of tea")

name = st.text_input("Enter your name")
if name:
    st.write(f"Welcome {name} ! your chai is on the way")

dob = st.date_input("Select your DOB")
st.write(f" Selected DOB {dob}")