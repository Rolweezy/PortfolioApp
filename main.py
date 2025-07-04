import streamlit as st

with st.sidebar:
    st.write("This is the sidebar")
st.set_page_config(
    layout= "wide",
    initial_sidebar_state= "expanded",
    page_title= "Ronald Oluoch Portfolio",
    #icon= ":crown:"
    )
st.title("Ronald Oluoch Portfolio Website")

dummy1, actual, dummy2 = st.columns([1,3,1])
with actual:
    st.write("Data Scientist| Data Analyst| Python Developer")

st.header("Personal Information")
#st.camera_input("Take an image of your photo")

col1, col2 = st.columns([1,2])
with col1:
    st.image("Ronald.jpeg")
with col2:
    st.subheader("General Information")
    st.text("I am a degree holder in bachelor of science, Actuarial Science with IT and a certified Data Analyst.")
    st.text("My knowledge skills entails statistical analysis with spss, programming with Java, Python and C++")
    st.text("My experience is broad and comprehensive with hands on dealing with data for analysis, planning and construction of prediction models in real life commercial space")

    st. subheader("Hobbies")
    st.write("Reading Ebooks")
    st.text("Writing Ebooks")
    st.text("Social Media")
    st.text("Trading Forex")










