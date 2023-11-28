import openai
import json
 

def runConversation(eventDescription):
    messages = [
        {
            "role": "system",
            "content": "Your are acting as an event planner guide specializing in software development domain. For any event type, you will generate the About Us section, Event Planner for the given event type."
        },
        {
            "role":"user",
            "content": f"Event Planner: {eventDescription}"
        }
    ]

    
    functions =[
        {
        "event_type" : "string",
        "event" : [
        {
            "event_title" : "string",
            "event_date" : "string",
            "event_location" : "string",
            "event_time" : "string",
            "event_audience" : "string",
            "event_link" : "string" 
        }
    ]
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

    # Save the parsed data to a JSON file
    with open('milestone_data.json', 'w') as f:
        json.dump(function_data, f, indent=4)
    
    return function_data