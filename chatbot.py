print("🤖 DecodeBot: Hello! Type 'exit' to quit.")

while True:
    user = " ".join(input("You: ").lower().split())

    if user == "hello" or user == "hi":
        print("🤖 DecodeBot: Hello!")

    elif user == "how are you":
        print("🤖 DecodeBot: I am fine.")

    elif user == "what is your name" or user == "your name":
         print("🤖 DecodeBot: My name is DecodeBot.")

    elif user == "what is ai":
         print("🤖 DecodeBot: AI stands for Artificial Intelligence.")
 
    elif user == "what is python":
         print("🤖 DecodeBot: Python is a programming language.")

    elif user == "thank you" or user == "thanks":
         print("🤖 DecodeBot: You're welcome!")

    elif user == "good morning":
         print("🤖 DecodeBot: Good morning!")

    elif user == "good night":
         print("🤖 DecodeBot: Good night!")
    
   
        
    elif user == "bye" or user == "exit" or user == "goodbye" :
        print("🤖 DecodeBot: Goodbye!")
        break

    else:
        print("🤖 DecodeBot: Sorry, I don't understand.")