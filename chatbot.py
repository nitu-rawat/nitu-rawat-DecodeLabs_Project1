print("🤖 Welcome to Rule-Based AI Chatbot")
print("Type 'bye' to exit")

while True:

    user = input("You: ").lower()

    if user == "hello":
        print("Bot: Hello! Nice to meet you.")

    elif user == "hi":
        print("Bot: Hi! How can I help you?")

    elif user == "how are you":
        print("Bot: I am fine. Thank you.")

    elif user == "what is ai":
        print("Bot: AI means Artificial Intelligence.")

    elif user == "your name":
        print("Bot: My name is DecodeLabs Bot.")

    elif user == "bye":
        print("Bot: Goodbye!")
        break

    else:
        print("Bot: Sorry, I don't understand.")