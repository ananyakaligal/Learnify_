from google.auth.transport.requests import Request
from google.oauth2.service_account import Credentials

# Path to your service account key file
key_path = './gen-lang-client-0838065725-01cb358183eb.json'

# Load credentials from the service account key file
credentials = Credentials.from_service_account_file(
    key_path,
    scopes=['https://www.googleapis.com/auth/cloud-platform']
)

# Refresh the credentials if they are expired
if credentials.expired:
    credentials.refresh(Request())

# Vertex AI Initialization (if needed)
# vertexai.init()

# Other constants
PROJECT_ID = 'gen-lang-client-0838065725'
REGION = 'us-central1'

from vertexai.preview.generative_models import GenerativeModel
import streamlit as st

# Initialize GenerativeModel
gemini_pro_model = GenerativeModel("gemini-1.0-pro")

def get_output(inputText: str):
    return gemini_pro_model.generate_content(inputText).text

def userInterface():
    st.title("Learnify")

    topic, des, diff, proef = aiNotesGenerator()
    if topic and des and diff and proef is not None:
        generatedNotes(topic, des, diff, proef)

def aiNotesGenerator():
    st.divider()
    st.header("Generate Notes with AI")
    topic = st.text_input("Topic", placeholder="Enter the topic")
    description = st.text_input("Description", placeholder="Enter a brief description about your topic")
    difficulty = st.text_input("Clearness", placeholder="Ex: easy, medium, hard")
    proefficiency = st.text_input("Proefficiency", placeholder="Beginner, Professional, etc.")

    generate = st.button("Generate notes!")

    if generate:
        return topic, description, difficulty, proefficiency
    else:
        return None, None, None, None

def generatedNotes(topic, desc, diff, poref):
    prompt = (f"Can you generate notes on the following things "
              f"Topic: {topic}, short description: {desc}, difficulty: {diff}, and proefficiency: {poref}")
    response = get_output(prompt)
    st.write(response)

userInterface()
