import streamlit as st
from transformers import pipeline

@st.cache(allow_output_mutation=True)
def get_model():
	return pipeline('text-generation', model='umarbutler/open-australian-legal-phi-1_5')

def generate(model, text):
	response = model(text)
	return response[0].get('generated_text') if response else 'No response'

st.title('Chat with AI')

usr_input = st.text_input('Your message')

if usr_input:
	model = get_model()
	response = generate(model, usr_input)
st.markdown(f'*AI*: {response}')
