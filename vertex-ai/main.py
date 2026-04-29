from google.genai import Client
from google.oauth2.service_account import Credentials

api_key_path="gen-lang-client-0633933490-5b5a557f04b4.json"
credentials=Credentials.from_service_account_file(api_key_path,scopes=["https://www.googleapis.com/auth/cloud-platform"])
PROJECT_ID="gen-lang-client-0633933490"
REGION="us-central1"
MODEL_NAME="gemini-2.5-pro"
client = Client(vertexai=True, project=PROJECT_ID, location=REGION,credentials=credentials)

response = client.models.generate_content(model=MODEL_NAME, contents="What is the capital of France?")
print(response.text)