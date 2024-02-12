import streamlit as st
import requests
import base64

# Function to get chat response
def get_chat_response(user_input):
    # Define API key and secret
    api_key_id = "client_0708c5956739ab6aac20d009f22126cb"
    api_key_secret = "IyTQUMiURS_y6f0CILNboHfryq_MvIggw4nH6ECelF0"
    
    # Encode credentials
    authToken = base64.b64encode(f"{api_key_id}:{api_key_secret}".encode("utf-8")).decode("utf-8")
    
    # Define the payload
    payload = {
        "input": user_input,
    }
    
    # Make the request
    response = requests.post(
        "https://api.superpowered.ai/v1/chat/threads/d2b42bd6-5adf-4261-9f8f-e013eb29e342/get_response",
        headers={"Authorization": f"Bearer {authToken}"},
        json=payload
    )
    
    # Check if the request was successful
    if response.status_code == 200:
        return response.json()["interaction"]["model_response"]["content"]
    else:
        return "Error: Unable to get response from the API."

# Initialize Streamlit app
def main():
    st.title("Chat with Our LLM")
    
    # Create a form for input
    with st.form("chat_form"):
        user_input = st.text_input("Type your message here")
        submit_button = st.form_submit_button("Send")
    
    # Get and display response
    if submit_button and user_input:
        chat_response = get_chat_response(user_input)
        st.write(chat_response)

if __name__ == "__main__":
    main()
