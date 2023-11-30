import json
import openai
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Set OpenAI API key
openai.api_key = os.getenv('OPEN_AI_KEY')
openai.organization = os.getenv('OPENAI_ORG_ID')

def load_json_events(file_path):
    with open(file_path, 'r') as f:
        return json.load(f)
    
events_data = load_json_events("events_data.json")

def event_chains(event_data):
    event_type = event_data['event_type']
    event_details = event_data['event'][0]
    event_title = event_details['event_title']
    event_date = event_details['event_date']
    event_location = event_details['event_location']
    event_time = event_details['event_time']
    event_audience = event_details['event_audience']
    event_link = event_details['event_link']

    # generated_events = []
    prompt_events = f"Generate the lists about of chain of events/Topics or Discussion Points for the {event_title} of the {event_type} in form of points, and No subpoints to included."

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are event planner. You change the plan according to the event type mentioned."},
            {"role": "user", "content": prompt_events},
        ]
    )

# Extract the content from the response and strip any leading/trailing whitespace
    generated_events = response['choices'][0]['message']['content'].strip()
    return generated_events


def create_dynamic_json(generated_events):
    # Assuming each event is separated by a newline character.
    event_titles = generated_events.split('\n')

    chain_of_events = {"ChainOfEvents": []}
    for idx, title in enumerate(event_titles, start=1):
        # Avoid adding empty strings as events.
        if title.strip():
            chain_of_events["ChainOfEvents"].append({"topicNumber": idx, "topicTitle": title.strip()})
    return chain_of_events


generated_events = event_chains(events_data)
print(generated_events)

dynamic_json = create_dynamic_json(generated_events)
with open("events_chains.json", 'w') as file:
    json.dump(dynamic_json, file, indent=4)