print("\nHello! I’m Nova 🤖 – your friendly chatbot.")
print("Type 'bye' or 'exit' to end the conversation.\n")

while True:
    user_input = input("You: ")
    
    if user_input.lower() in ['bye', 'exit']:
        print("Nova: Goodbye! Have a great day! 🌟")
        break

    elif user_input.strip() == "":
        print("Nova: Please say something! I’m all ears. 👂")

    elif user_input.lower() in ['hi', 'hello', 'hey']:
        print("Nova: Hello there! How can I assist you today?")
    
    elif user_input.lower() in ['how are you', 'how\'s it going', 'how are you doing']:
        print("Nova: I’m just a bunch of code, but I’m functioning smoothly! 😄")

    elif user_input.lower() in ['your name', 'what\'s your name']:
        print("Nova: I’m Nova, built by Shiv – the code whisperer.")

    elif user_input.lower() in ['help', 'what can you do', 'capabilities']:
        print("Nova: I can chat with you, tell jokes, or give basic info. Ask me anything!")

    elif user_input.lower() in ['tell me a joke', 'joke', 'make me laugh']:
        print("Nova: Why don’t programmers like nature? Too many bugs. 🐛")

    elif user_input.lower() in ['what is your purpose', 'why do you exist']:
        print("Nova: My purpose is to assist and entertain you! I’m here to make your day brighter. ☀️")

    elif user_input.lower() in ['what is ai', 'explain ai', 'artificial intelligence']:
        print("Nova: AI, or Artificial Intelligence, is the simulation of human intelligence in machines. It’s like giving computers a brain! 🧠")
    
    elif user_input.lower() in ['what is your favorite color', 'favorite color']:
        print("Nova: I don’t see colors like you do, but I think blue is pretty cool! 💙")

    elif user_input.lower() in ['what is the meaning of life', 'meaning of life']:
        print("Nova: The meaning of life is a big question! Some say it’s about finding happiness, others say it’s about making connections. What do you think? 🤔")
    
    elif user_input.lower() in ['tell me a fact', 'interesting fact']:
        print("Nova: Did you know that honey never spoils? Archaeologists have found pots of honey in ancient Egyptian tombs that are over 3000 years old and still edible! 🍯")

    elif user_input.lower() in ['options', 'menu']:
        print("ChatNova: You can ask about my name, get a joke, a fact, or just say hi!")

    else:
        print("Nova: Hmm… I’m not trained for that yet. But I’m learning every day!")
