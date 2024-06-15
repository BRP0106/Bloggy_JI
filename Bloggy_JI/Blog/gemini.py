import google.generativeai as genai

# Configure the API key
genai.configure(api_key="AIzaSyCtbOt72ZGcY_AZruXrVK8bNE2IRqok8WE")

# Set up generation configuration
generation_config = {
    "temperature": 0.9,
    "top_p": 1,
    "top_k": 1,
    "max_output_tokens": 2048,
}

# Set up safety settings
safety_settings = [
    {
        "category": "HARM_CATEGORY_HARASSMENT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
    {
        "category": "HARM_CATEGORY_HATE_SPEECH",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
    {
        "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
    {
        "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
]

# Initialize the model
model = genai.GenerativeModel(model_name="gemini-1.0-pro",
                              generation_config=generation_config,
                              safety_settings=safety_settings)

# Start a conversation with an empty history
convo = model.start_chat(history=[])

# Define exit keyword
exit_keywords = ['exit', 'quit', 'bye']

while True:
    # User input
    user_input = input("You: ")

    # Check if the user wants to exit
    if user_input.lower() in exit_keywords:
        print("Goodbye!")
        break

    # Send user input to the model
    convo.send_message(user_input)

    # Print the model's response
    print("AI: " + convo.last.text)
