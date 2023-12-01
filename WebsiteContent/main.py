from faqs.events_faqs import get_faqs
from description.event_description import event_description


if __name__ == "__main__":
    description = event_description(faqs_data)
    faqs = get_faqs()
    for faq in faqs:
        print(f"Q: {faq['question']}\nA: {faq['answer']}\n")

