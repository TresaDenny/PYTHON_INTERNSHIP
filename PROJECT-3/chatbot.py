'''BUILD A CHATBOT USING NATURAL
LANGUAGE PROCESSING LIBRARIES LIKE
NLTK OR SPACY, CAPABLE OF ANSWERING
USER QUERIES.'''

import nltk
from nltk.chat.util import Chat, reflections

# Download NLTK data (only needed the first time)
nltk.download('punkt')

# Define pairs of patterns and responses
pairs = [
    [
        r"hi|hello|hey",
        ["Hello! How can I help you today?", "Hi there! What can I do for you?"]
    ],
    [
        r"what is your name ?",
        ["I am a chatbot created using NLTK.",]
    ],
    [
        r"how are you ?",
        ["I'm doing well, thank you!", "I'm a bot, but I'm here to help!"]
    ],
    [
        r"(.*) your name ?",
        ["My name is NLTK Chatbot.",]
    ],
    [
        r"(.*) (help|support) (.*)",
        ["Sure, I'm here to help. Please tell me your query."]
    ],
    [
        r"quit|exit|bye",
        ["Goodbye! Have a nice day.", "Bye!"]
    ],
    [
        r"(.*)",
        ["Sorry, I didn't understand that. Can you rephrase?"]
    ]
]

def chatbot():
    print("Hi! I'm your chatbot. Type 'quit' to exit.")
    chat = Chat(pairs, reflections)
    chat.converse()

if __name__ == "__main__":
    chatbot()
