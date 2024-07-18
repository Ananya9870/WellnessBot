import streamlit as st
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import random

# Download the VADER lexicon
nltk.download('vader_lexicon')

# Initialize SentimentIntensityAnalyzer
sid = SentimentIntensityAnalyzer()

# Define responses and therapeutic strategies
positive_responses = ["That's great!", "Good to hear!", "Keep it up!"]
negative_responses = ["I'm sorry to hear that.", "That must be tough.", "I'm here to listen."]
therapeutic_strategies = {
    'identify_negative_thoughts': ["Let's identify any negative thoughts you're having."],
    'challenge_negative_thoughts': ["Let's challenge those negative thoughts together."],
    'practice_relaxation': ["Let's try a relaxation exercise."],
}

problem_solutions = {
    'stress': ["Try deep breathing exercises.", "Consider taking short breaks throughout your day.", "Practice mindfulness meditation."],
    'anxiety': ["Try progressive muscle relaxation techniques.", "Consider cognitive reframing exercises.", "Practice grounding techniques."],
    'depression': ["Engage in regular physical activity.", "Consider journaling about your feelings.", "Connect with supportive friends or family members."],
}

# Function to analyze sentiment of user input
def analyze_sentiment(message):
    scores = sid.polarity_scores(message)
    compound_score = scores['compound']
    if compound_score >= 0.05:
        return 'positive'
    elif compound_score <= -0.05:
        return 'negative'
    else:
        return 'neutral'

# Function to respond based on user's emotional state
def generate_response(user_input):
    sentiment = analyze_sentiment(user_input)
    if sentiment == 'positive':
        return random.choice(positive_responses)
    elif sentiment == 'negative':
        for problem, solutions in problem_solutions.items():
            if problem in user_input.lower():
                feedback = random.choice(negative_responses)
                solution = random.choice(solutions)
                therapeutic_strategy = random.choice(therapeutic_strategies[random.choice(list(therapeutic_strategies.keys()))])
                return f"{feedback} Here's a solution for '{problem}': {solution}. {therapeutic_strategy}"
        feedback = random.choice(negative_responses)
        therapeutic_strategy = random.choice(therapeutic_strategies[random.choice(list(therapeutic_strategies.keys()))])
        return f"{feedback} {therapeutic_strategy}"
    else:
        return "I understand."

# Streamlit app
def main():
    st.title("MindfulBot")
    st.write("Welcome to MindfulBot. How can I help you today?")

    user_input = st.text_input("You:", "")

    if st.button("Submit"):
        response = generate_response(user_input)
        st.write("MindfulBot:", response)

if __name__ == "__main__":
    main()