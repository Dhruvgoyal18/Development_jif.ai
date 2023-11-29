from json_generation_event import runConversation, functions  # Import runConversation and functions

def get_content():
    eventDescription = "Conduct a Seminar on Stock Management on 30th November at Lakshmi Auditorium at 06:00 pm."
    result = runConversation(eventDescription, functions)  # Pass functions as an argument
    print(result)

get_content()
