import streamlit as st
st.title("Food Recommendation App")

# Text input for user query
user_input = st.text_input("What type of food are you looking for?")

# Button to submit query
if st.button("Get Recommendations"):
    # Here, you would call your backend function to get recommendations
    recommendations = ["Example Restaurant 1", "Example Restaurant 2"]  # Replace with actual logic
    st.write("Recommendations:")
    for restaurant in recommendations:
        st.write(restaurant)