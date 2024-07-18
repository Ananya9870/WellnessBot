WellnessBot: AI-Powered CBT Therapy for emotional wellbeing.

An AI based model for mental health. This model is a simple therapeutic chatbot designed to respond to user input based on sentiment analysis using NLTK's VADER sentiment intensity analyzer. This chatbot provides positive or negative responses based on the sentiment of user's input and offers therapeutic strategies and solutions for specific problems.
Takes a message as input and returns 'positive', 'negative', or 'neutral' based on the sentiment score.

NLTK is a powerful library for natural language processing (NLP).
VADER ( Valence Aware Dictionary and sEntiment Reasoner) is specially attuned to sentiments expressed in social media.

Import streamlit.

chat(): Main loop for user interaction. It continuously prompts the user for input, analyzes the sentiment, and provides an appropriate response until the user types 'quit', 'exit', or 'bye'.
