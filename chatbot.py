
def chatbot_response(user_input):
    user_input = user_input.lower()
    if "hello" in user_input:
        return "HI!"
    elif "how are you" in user_input:
        return "I'm fine, thanks!"
    elif "bye" in user_input:
        return "Goodbye!"
    
def start_chat():
    print("Chatbot: Hello! Type 'bye' to exit." )

    while True:
        user_message = input("you: ")

        response = chatbot_response(user_message)
        print(f"chatbot: {response}")

        if "bye" in user_message.lower():
            break

if __name__ == "__main__":
    start_chat()