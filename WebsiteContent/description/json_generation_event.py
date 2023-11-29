import openai
import json
from dotenv import load_dotenv
import os
load_dotenv()

openai.api_key = os.getenv('OPEN_AI_KEY')

def load_json_schema(file_path):
    with open(file_path, 'r') as f:
        schema_content = json.load(f)
        # Wrap the schema content into a function definition
        function_definition = {
            "name": schema_content["name"],  
            "parameters": schema_content["parameters"]
        }
        return [function_definition]

    
functions = load_json_schema("events_schema.json")

def runConversation(eventDescription, functions):
    messages = [
        {
            "role": "system",
            "content": "You are acting as an event planner guide specializing in the software development domain. For any event type, you will generate the About Us section and Event Planner for the given event type."
        },
        {
            "role": "user",
            "content": f"Event Planner: {eventDescription}"
        }
    ]

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo-0613",
        messages=messages,
        functions=functions,
        function_call="auto",
    )
    
    response_message = response["choices"][0]["message"]
    function_data = json.loads(response_message['function_call']['arguments'])
    
    with open('events_data.json', 'w') as f:
        json.dump(function_data, f, indent=4)
    
    return function_data
