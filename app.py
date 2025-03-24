import streamlit as st

# Configure the webpage
st.set_page_config(page_title="Quoria Introduction and Tutorials", layout="centered")

st.title("Quoria Introduction and Tutorials")
st.write("Welcome to the introduction and tutorial page for Quoria.")

# Product Description
st.header("About Quoria")
st.write("Quoria is an advanced chatbot designed to assist users with various tasks and provide intelligent responses.")
st.image("https://via.placeholder.com/600x300", caption="Quoria Interface")

# User Guide
st.header("How to Use Quoria")
st.write("1. Start a conversation with Quoria.\n2. Ask questions or request assistance.\n3. Follow the guidance provided by Quoria.")

# Contact Information
st.header("Contact Us")
st.write("If you have any questions or need support, please reach out to us via email or hotline.")
st.write("Email: support@example.com")
st.write("Hotline: 0123-456-789")

st.write("---")
st.info("Thank you for your interest in Quoria!")
