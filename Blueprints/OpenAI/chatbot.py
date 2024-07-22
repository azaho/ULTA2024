from openai import OpenAI

def chatbot():
    client = OpenAI()
    
    system_message = "You are a helpful assistant."
    messages = [{"role": "system", "content": system_message}]
    
    print("Welcome to the fantastically phenomenal ULTA 2024 chatbot.")
    print("Type 'quit' to exit the conversation.")
    
    while True:
        user_input = input("> ")
        
        if user_input.lower() in ['q', 'quit']:
            break
        
        messages.append({"role": "user", "content": user_input})
        
        try:
            completion = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=messages
            )
            
            assistant_response = completion.choices[0].message.content
            print("\n", assistant_response)
            
            messages.append({"role": "assistant", "content": assistant_response})
            
        except Exception as e:
            print(f"An error occurred: {e}")
            break

if __name__ == "__main__":
    chatbot()
