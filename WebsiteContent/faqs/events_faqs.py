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

def generate_questions(description, num_questions=7):
    # Instruct OpenAI to generate questions about the event
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=f"Given this event description, generate {num_questions} relevant questions:\n\nDescription: {description}\n\nQuestions:",
        max_tokens=150
    )

    questions = response.choices[0].text.strip().split('\n')
    return questions


def get_faqs(description):
    questions = generate_questions(description)
    faqs = []

    for question in questions:
        if not question.strip(): 
            continue

        # Generate an answer for each question
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=f"Description: {description}\n\nQuestion: {question}\nAnswer:",
            max_tokens=100
        )

        answer = response.choices[0].text.strip()

            # Add the question and answer to the FAQs list
        faqs.append({"question": question, "answer": answer})

    return faqs

# Example 
description = "Attention Stock Managers, Inventory Controllers, and Warehouse Managers! Join us at Lakshmi Auditorium on November 30th at 06:00 pm for a Stock Management Seminar. Enhance your skills and stay updated on the latest industry practices. Don't miss out on this opportunity!"
faqs = get_faqs(description)
for faq in faqs:
    print(f"Q: {faq['question']}\nA: {faq['answer']}\n")


