# Step 1: Import necessary libraries
import streamlit as st
import superpowered
import os

# Step 2: Set up API keys (These should ideally be environment variables or securely stored)
os.environ["SUPERPOWERED_API_KEY_ID"] = "client_0708c5956739ab6aac20d009f22126cb"
os.environ["SUPERPOWERED_API_KEY_SECRET"] = "IyTQUMiURS_y6f0CILNboHfryq_MvIggw4nH6ECelF0"

# Initialize Streamlit app
def main():
    st.title("Chat with Our LLM")

    # Step 3: Create a form for input
    with st.form("chat_form"):
        user_input = st.text_input("Type your message here")
        submit_button = st.form_submit_button("Send")

    if submit_button and user_input:
        # Step 4: Make the request and get the response
        response = superpowered.get_chat_response(
            thread_id="d2b42bd6-5adf-4261-9f8f-e013eb29e342",
            input=user_input,
        )
        
        # Step 5: Display the response
        if response and 'interaction' in response and 'model_response' in response['interaction']:
            st.write(response["interaction"]["model_response"]["content"])
        else:
            st.write("There was an error processing your request.")

if __name__ == "__main__":
    main()
