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

def get_attendee_types(description, num_types=5):
    # Generate attendee types using OpenAI's API
    prompt = f"Based on an event with the following description: '{description}', generate {num_types} types of potential attendees:"
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=100
    )

    types = response.choices[0].text.strip().split('\n')
    return [attendee_type.strip() for attendee_type in types if attendee_type.strip()]

def get_attendee_descriptions(description):
    attendee_types = get_attendee_types(description)

    attendee_info = {}

    for attendee_type in attendee_types:
        # Generate a description for each type of attendee
        prompt = f"Provide a brief description for {attendee_type} who might attend an event about {description}"
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=60
        )

        generated_description = response.choices[0].text.strip()

        # Store the generated description in a dictionary
        attendee_info[attendee_type] = generated_description

    return attendee_info

# Example usage
description = "Stock Management Seminar"
attendee_descriptions = get_attendee_descriptions(description)
for attendee_type, desc in attendee_descriptions.items():
    print(f"{attendee_type.title()}: {desc}\n")
