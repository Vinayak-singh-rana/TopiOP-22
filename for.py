import streamlit as st
with st.form("form"):
    st.write("fill the form")
    name = st.text_input("name")
    collegename = st.text_input("your college name")
    percentage = st.number_input("your percentage")
    working = st.checkbox("are you working")

    submitted = st.form_submit_button("submit")
    if submitted:
        st.write("name", name)
        st.write("college name", collegename)
        st.write("percentage", percentage)
        st.write("r u working", working)



