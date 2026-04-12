import streamlit as st

st.title("Chai Taste Poll")

col1, col2 = st.columns(2)

with col1 :
    st.header("Masala Chai")
    st.image("https://images.pexels.com/photos/36991440/pexels-photo-36991440.jpeg?_gl=1*nqhkx1*_ga*MzgzNzU0MDMwLjE3NDA1MTI0ODk.*_ga_8JE65Q40S6*czE3NzYwMjMzNzUkbzkkZzEkdDE3NzYwMjMzODUkajUwJGwwJGgw", width=200)
    vote1 = st.button("Vote Masala chai")

with col2:
    st.header("Adrak Chai")
    vote2 = st.button("Vote Adrak chai")

if vote1:
    st.success("Thanks for voting masala chai ")

elif vote2:
    st.success("Thanks for voting adrak chai")

