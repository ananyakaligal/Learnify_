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

    userInput = aiSummariser()
    if userInput is not None:
        summarisedContent(userInput)


def aiSummariser():
    st.header("AI Summariser")
    content = st.text_area(" ", label_visibility='hidden', placeholder="Paste your text here")
    summarise = st.button("Summarise!")
    if summarise:
        return content
    else:
        return None


def summarisedContent(summary: str):
    st.header("Summarised content!")
    prompt = f"Can you summarise this text for me? In simple and easy way? and in Structured way? {summary}"
    respones = get_output(prompt)
    st.write(respones)


userInterface()

