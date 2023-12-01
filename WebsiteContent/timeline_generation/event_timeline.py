import json
import openai
from dotenv import load_dotenv
import os
from datetime import datetime, timedelta
# Load environment variables
load_dotenv()

# Set OpenAI API key
openai.api_key = os.getenv('OPEN_AI_KEY')
openai.organization = os.getenv('OPENAI_ORG_ID')

def load_json_events(file_path):
    with open(file_path, 'r') as f:
        return json.load(f)
    
events_chains = load_json_events("../description/events_chains.json")


def get_timeline(start_date, start_time="09:00 AM", topic_duration_hours=1, break_duration_minutes=15):
    timeline = []
    current_date = datetime.strptime(start_date, "%Y-%m-%d")
    current_time = datetime.strptime(start_time, "%I:%M %p")
    end_of_day = datetime.strptime("05:00 PM", "%I:%M %p")

    for event in events_chains['ChainOfEvents']:
        # Generate a short description for each topic
        description = f"Discussion and insights on {event['topicTitle']}. This session covers key concepts, strategies, and best practices."

        timeline_entry = {
            "date": current_date.strftime("%Y-%m-%d"),
            "time": current_time.strftime("%I:%M %p"),
            "topicNumber": event["topicNumber"],
            "topicTitle": event["topicTitle"],
            "description": description
        }
        timeline.append(timeline_entry)

        # Increment the time for the next topic
        current_time += timedelta(hours=topic_duration_hours, minutes=break_duration_minutes)
        
        # If the next topic extends beyond the end of the day, move it to the next day
        if current_time.time() > end_of_day.time():
            current_date += timedelta(days=1)
            current_time = datetime.combine(current_date, datetime.strptime(start_time, "%I:%M %p").time())

    return timeline


def get_json(file_path):
    with open(file_path, 'w') as file:
        json.dump(timeline, file, indent=4)

# Generating and saving the timeline
timeline = get_timeline("2023-12-01")

get_json("events_timeline.json")

