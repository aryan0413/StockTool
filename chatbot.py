import streamlit as st
import google.generativeai as genai

# Set up Google Generative AI API key
genai.configure(api_key="AIzaSyCSYrnfRG5E7sMDMzwB2nIln66F2Ns6UQA")

# Initialize the generative model
model = genai.GenerativeModel("gemini-1.5-flash")

# Streamlit interface
st.title("AI Chatbot")

# Get user input
user_input = st.text_input("You: ", "")

# If user input is not empty, generate a response from the AI model
if user_input:
    response = model.generate_content(user_input)
    st.write("AI: ", response.text)
