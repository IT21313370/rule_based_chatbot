from flask import Flask, render_template, request, jsonify
import nltk
from nltk.tokenize import word_tokenize
import json

app = Flask(__name__)

# Load your predefined responses
predefined_responses = {
    "hi": "Hello! How can I assist you today?",
    "hello": "Hi there! How can I help you?",
    "hey": "Hey! What can I do for you today?",
    "bye": "Goodbye! Have a wonderful day ahead!",
    "goodbye": "See you later! Take care!",
    "how are you": "I'm just a bot, but I'm doing well! Thanks for asking. How about you?",
    "what is your name": "I am your assistant bot, here to help you with whatever you need!",
    "what can you do": "I can answer your questions, provide information, or just chat! What would you like to do?",
    "tell me a joke": "Sure! Why don't skeletons fight each other? They don't have the guts!",
    "who created you": "I was created by a team of developers to assist and provide helpful responses!",
    "what time is it": "I can't tell the time, but you can check it on your device's clock!",
    "how can I help you": "I’m here to assist you with anything you need. How can I assist you today?",
    "thank you": "You're welcome! I'm happy to help anytime.",
    "thanks": "No problem! Let me know if you need anything else.",
    "sorry": "No worries! It's all good. How can I assist you further?",
    "help": "Sure! I'm here to help. What do you need assistance with?",
    "how do you work": "I process your messages and provide responses based on predefined answers or logic. Just ask me anything!",
    "what is the weather like": "I’m not able to get the weather, but you can check it on your favorite weather app.",
    "can you tell me the news": "I don't have access to the latest news, but you can easily find it on news websites or apps.",
    "who are you": "I’m an assistant bot designed to help you out with anything you need!",
    "what is your purpose": "My purpose is to assist you, answer questions, and provide help wherever I can.",
    "do you understand me": "Yes, I can understand your messages and respond accordingly. Let me know how I can help!",
    "do you have emotions": "I don't have emotions like humans, but I try to respond in a friendly and helpful way!",
    "can you learn": "I’m designed to follow predefined responses, but I can adapt based on the information you provide.",
    "what is your favorite color": "I don't have preferences, but I think blue is a nice color. What about you?",
    "tell me something interesting": "Did you know? Honey never spoils! Archaeologists have found pots of honey in ancient tombs that are still edible!",
    "what is the meaning of life": "That’s a deep question! Many people have different answers, but for me, it’s to assist you as best as I can!",
    "can you talk to me": "Of course! I’m here to chat with you. What would you like to talk about?",
    "what can I ask you": "You can ask me anything! From general knowledge to personal help, I’ll try my best to assist you.",
    "are you real": "I’m not a human, but I’m real in the sense that I exist to help you in any way I can.",
    "can you help with tasks": "I can assist with various tasks, like answering questions or helping you find information. What do you need help with?",
    "can you play music": "I can't play music directly, but I can suggest songs or playlists if you'd like!",
    "what do you like to do": "I don’t have personal preferences, but I love helping out with your questions and tasks!",
    "tell me a fun fact": "Did you know? An octopus has three hearts! Two pump blood to the gills, and one pumps it to the rest of the body.",
    "can you make a joke about me": "I’d rather not, but I can tell you another joke if you’d like!",
    "what do you think of humans": "Humans are fascinating! They have creativity, emotion, and intelligence that inspire everything I do.",
    "are you a human": "No, I’m an AI bot created to assist you with tasks and provide helpful information.",
    "what is AI": "AI, or Artificial Intelligence, refers to machines or software that can perform tasks that typically require human intelligence, like learning and problem-solving.",
    "how do I contact support": "You can reach support through the help section or by contacting the support team directly through their website or email.",
    "can you provide recommendations": "Sure! What would you like recommendations for? Movies, books, places to visit, or something else?"
}


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.form["message"]
    response = get_bot_response(user_message)
    return jsonify({"response": response})

def get_bot_response(user_message):
    user_message = user_message.lower()  # Convert message to lowercase
    for key in predefined_responses:
        if key in user_message:
            return predefined_responses[key]
    return "Sorry, I didn't understand that."

if __name__ == "__main__":
    app.run(debug=True)
