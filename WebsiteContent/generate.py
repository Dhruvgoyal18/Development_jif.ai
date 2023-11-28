from description.content import runConversation

def get_content():
    eventDescription = "Conduct a Seminar on Stock Management on 30th November at Lakshmi Auditorium at 06:00 pm."

    result = runConversation(eventDescription)
    print(result)

get_content()










