# Project 1: Rule-Based Chatbot
# Description: A simple chatbot that responds to predefined user inputs
# using a dictionary and conditional statements.


# Store predefined user inputs (keys) and chatbot responses (values).
responses = {
  "hello": "Hello! How can I assist you today?",
  "what is your name": "I'm ChatBot, your assistant.",
  "how are you": "I'm functioning perfectly! Thanks for asking.",
  "what can you do": "I can answer basic questions and have simple conversations.",
  "who created you": "I was developed as part of an AI internship project.",
  "good morning": "Good morning! Have a wonderful day!",
  "good evening": "Good evening! How can I help you?",
  "thank you": "You're welcome! Happy to help.",
  "thanks": "My pleasure!",
  "goodbye": "Goodbye! Have a great day!",
  "what is ai": "AI stands for Artificial Intelligence.",
  "what is python": "Python is a popular programming language.",
  "are you human": "No, I'm a rule-based chatbot.",
  "can you learn": "No, I follow predefined rules.",
  "how do you work": "I match your input with predefined responses.",
  "tell me a joke": "Why do programmers prefer dark mode? Because light attracts bugs!",
  "motivate me": "Every expert was once a beginner. Keep going!",
  "who is your developer": "I was developed by an AI internship student.",
  "what is your purpose": "My purpose is to demonstrate rule-based AI.",
  "help": "You can ask about me, programming, or AI."
}

# Display instructions when the chatbot starts.
print("Enter prompt or 'exit' to end chat.")

# Keep the chatbot running until the user enters the exit command.
while True:

  # Accept user input, convert it to lowercase, and remove
  # leading and trailing whitespace for consistent matching.
  user_input = input("You: ").lower().strip()

  # Check whether the user wants to end the conversation.
  if user_input == "exit":
    print("Chat completed!")
    break # Terminate the loop and end the program.
    
  else:
    # Search for the user's input in the responses dictionary.
    # Return a default message if no matching key is found.
    reply = responses.get(user_input, "Sorry! I don't understand.")

    # Display the chatbot's response.
    print("ChatBot:", reply)
