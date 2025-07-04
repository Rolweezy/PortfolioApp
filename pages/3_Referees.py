import streamlit as st

st.title("Referees")
st.subheader("1.")

col1, col2 = st.columns([1,5])
with col1:
    st.image("mary_joe.jpeg", width=200)
with col2:
    st.write("Mary Joe")
    st.write("Phone Number: 0734786512")
    st.write("Email Address: maryjoe@gmail.com")

st.divider()
st.subheader("2.")
col1_2, col2_2= st.columns([1,5])
with col1_2:
    st.image("joseph.jpeg", width =200)
with col2_2:
    st.write("Joseph Ochieng'")
    st.write("Phone Number: 0734928711")
    st.write("Email Address: jochieng'@gmail.com")

st. divider()
st.subheader("3.")
col1_3, col2_3 = st.columns([1,5])
with col1_3:
    st.image("maina.jpeg", width=200)
with col2_3:
    st.write("James Maina")
    st.write("Phone Number: 011045673")
    st.write("Email Address: jamesmaina@gmail.com")

