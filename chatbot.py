print("Welcome to AI Chatbot!")
print("Type 'bye' to exit.")

while True:
    user = input("You: ").lower()

    if user == "bye":
        print("Bot: Goodbye!")
        break
    elif "hello" in user or "hi" in user:
        print("Bot: Hello! How can I help you?")
    elif "name" in user:
        print("Bot: I am a simple AI chatbot.")
    elif "ai" in user:
        print("Bot: AI means Artificial Intelligence.")
    elif "how are you" in user:
        print("Bot: I am working well!")
    else:
        print("Bot: Sorry, I don't understand that yet.")
