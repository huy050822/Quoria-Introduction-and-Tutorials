import streamlit as st

st.set_page_config(page_title="Quoria Introduction and Tutorials", page_icon="https://raw.githubusercontent.com/huy050822/Quoria-Chatbot/refs/heads/main/11zon_cropped.png", layout="centered")

st.title("Quoria Introduction and Tutorials")
st.write("Welcome to the introduction and tutorial page for Quoria.")

st.header("About Quoria")
st.write("QUORIA is an intelligent chatbot that helps users determine the value of a used motorcycle based on real-world data. Using a Linear Regression model and data sourced from Aiven Cloud, the bot can analyze key factors such as brand, model, year of manufacture, mileage, and condition to provide the most reasonable price estimate. Since this is a project developed by students, we would greatly appreciate any feedback if you have the opportunity to try it out!")
st.image("https://raw.githubusercontent.com/huy050822/Quoria-Introduction-and-Tutorials/refs/heads/main/Screenshot%202025-03-28%20082422.png", caption="Quoria Interface")

st.header("How to Use Quoria")
st.write(
    "1. **Start a conversation** with Quoria.\n"
    "2. **Enter Motorcycle Information**: Users need to provide basic details about the used motorcycle, including:\n"
    "   - Model\n"
    "   - Brand\n
    "   - Year of manufacture\n"
    "   - Kilometer\n"
    "   - Brand\n"
    "3. **Receive the Price Estimate**."
)
st.header("Contact Us")
st.write("If you have any questions or need support, please reach out to us via email or hotline.")
st.write("Email: huy.tnq@gmail.com")
st.write("Hotline: 0943001336")

st.write("---")
st.info("Thank you for your interest in Quoria!")
