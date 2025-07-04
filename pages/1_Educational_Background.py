import streamlit as st

st.title("Educational Background")

col1, col2= st.columns(2)
with col1:
    st.header("1")
    st.subheader("Bachelor of Actuarial Science With IT")
    with st.expander("Click to see more details"):
        st.write("Jaramogii Oginga Odinga University Of Science And Technology")
        st.write("January 2014- March 2018")
        st.write("Honour : 1st Class Honors")

    st.header("2")
    st.subheader("Certificate in Data Science")
    with st.expander("Click to see more details"):
        st.write("Emobilis School of Technology")
        st.write("May 2025- August 2025")
        st.write("Honour : 1st Class Honors")
with col2:
    st.header("3")
    st.subheader("Kenya Certificate Of Secondary Education")
    with st.expander("Click to see more details"):
        st.write("St. Mary's School Yala")
        st.write("January 2009- December 2012")
        st.write("Grade: A-")

    st.header("3")
    st.subheader("Kenya Certificate Of Primary Education")
    with st.expander("Click to see more details"):
        st.write("St. Anne's Ahero Primary SChool")
        st.write("January 2014- March 2018")
        st.write("Mean Grade : B-")