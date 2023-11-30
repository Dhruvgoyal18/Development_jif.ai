import json
import openai
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Set OpenAI API key
openai.api_key = os.getenv('OPEN_AI_KEY')
openai.organization = os.getenv('OPENAI_ORG_ID')

# Function to load JSON data from a file
def load_json_events(file_path):
    with open(file_path, 'r') as f:
        return json.load(f)


# functions = load_json_events("/description/events_data.json")
events_data = load_json_events("events_data.json")
def event_description(event_data):
    # Extracting details from the passed event data
    event_type = event_data['event_type']
    event_details = event_data['event'][0]
    event_title = event_details['event_title']
    event_date = event_details['event_date']
    event_location = event_details['event_location']
    event_time = event_details['event_time']
    event_audience = event_details['event_audience']
    event_link = event_details['event_link']

    # Constructing the prompt
    prompt = f"I want to conduct an {event_type} on the {event_title} at {event_location} on {event_date} & {event_time}. This is specifically targeted for {event_audience} and details about the {event_link}. Generate a prompt message of about 40 words to convey this information."

    # Generating the description using OpenAI
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # Adjust the model if necessary
        messages=[
            {"role": "system", "content": "You are a chat-based AI."},
            {"role": "user", "content": prompt},
        ]
    )

    generated_description = response['choices'][0]['message']['content'].strip()

    return generated_description

# Example usage of the function
generated_description = event_description(events_data)
print(generated_description)