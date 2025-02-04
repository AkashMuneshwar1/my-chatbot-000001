from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

# chatbot_logic.py

# Question flow (context-aware)
question_flow = {
    None: ["Hello", "Hi","Hi"],
    "Hello": ["How are you?", "What can you do?"],
    "Hi": ["How are you?", "What can you do?"],
    "I need help": ["Tell me about yourself", "What services do you provide?"],
    "How are you?": ["Goodbye", "Thank you"],
    "What can you do?": ["I need help", "Goodbye"],
    "Goodbye": [],
    "Thank you": ["Goodbye"],
    "Tell me about yourself": ["What can you do?", "Goodbye"],
    "What services do you provide?": ["Goodbye", "I need help"],
}

responses = {
    "Hello": "Hi there! How can I assist you today?",
    "Hi": "Hello! What can I help you with?",
    "How are you?": "I'm just a chatbot, but I'm here to help you!",
    "What can you do?": "I can answer your predefined questions and guide you.",
    "Goodbye": "Goodbye! Have a great day!",
    "I need help": "Sure, let me assist you. What do you need help with?",
    "Thank you": "You're welcome! Let me know if you need anything else.",
    "Tell me about yourself": "I'm your friendly chatbot, designed to answer your questions.",
    "What services do you provide?": "I can answer questions and guide you to helpful resources.",
}

def get_response_and_next_questions(current_question):
    return (
        responses.get(current_question, "I'm sorry, I don't understand that question."),
        question_flow.get(current_question, []),
    )
