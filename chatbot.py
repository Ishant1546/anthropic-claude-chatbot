import anthropic

# Initialize the Anthrop client
client = anthropic.Anthropic(api_key='<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>')

conversation = []

while True:
    user_message = input("You: ")

    if user_message.lower() == 'exit':
        print("Chat ended. Goodbye!")
        break

    # Add user message to the conversation
    conversation.append({'role': 'user', 'content': user_message})

    response = client.messages.create(
        model='claude-3-5-sonnet-20241022',
        max_tokens=1024,
        messages=conversation
    )

    bot_message = response.content[0].text
    print(f"Claude: {bot_message}")

    # Add chatbot response to the conversation
    conversation.append({'role': 'assistant', 'content': bot_message})
