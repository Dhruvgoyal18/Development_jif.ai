import json
import openai
from dotenv import load_dotenv
import os

load_dotenv()

# Set OpenAI API key
openai.api_key = os.getenv('OPEN_AI_KEY')
openai.organization = os.getenv('OPENAI_ORG_ID')

def load_json(file_path):
    with open(file_path, 'r') as f:
        return json.load(f)
    
def get_contact():
    # Sample contact information for three individuals
    contacts = [
        {"name": "John Doe", "email": "john.doe@example.com", "mobile": "123-456-7890"},
        {"name": "Jane Smith", "email": "jane.smith@example.com", "mobile": "234-567-8901"},
        {"name": "Alex Johnson", "email": "alex.johnson@example.com", "mobile": "345-678-9012"}
    ]
    for contact in contacts:
        print(f"\nName: {contact['name']}\nEmail: {contact['email']}\nMobile: {contact['mobile']}")

# Example usage
get_contact()
