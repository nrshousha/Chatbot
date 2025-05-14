import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
api_key = os.getenv("OPENROUTER_API_KEY") 

client = OpenAI(
    api_key=api_key,
    base_url="https://openrouter.ai/api/v1"  
)

def create_prompt(user_input, mood="default"):  # Create the prompt that we will send to ChatGPT.

    if mood == "sarcastic":
        return f"Respond with a sharp, witty, and sarcastic tone to this input, without adding any stage directions or actions like *eye roll* or *wipes brow*: {user_input}"
    elif mood == "enthusiastic":
        return f"Wow! That sounds exciting! Let's go! {user_input}"
    elif mood == "serious":
        return f"Let's analyze this seriously: {user_input}"
    else:
        return user_input
    
    
def ask_for_mood():
    """Function to ask user for mood."""
    mood = input("Choose mood (default / sarcastic / enthusiastic / serious): ").strip().lower()
    return mood

def get_ai_response(user_input, mood="default"):  # prepares the prompt, sends it, and gets the response
    
    prompt = create_prompt(user_input, mood)  # build the prompt based on the user's mood

    try:  # Submit a request to OpenAI
        response = client.chat.completions.create(
            model="mistralai/mistral-7b-instruct",
            messages=[
                {"role": "user", "content": prompt}
            ],
            max_tokens=150,  # Maximum number of words in a reply.
            temperature=0.7  # Randomness score (0.7 = balanced, 0 = very serious, 1 = more random)
        )
        
        # print("Full Response:", response)  # Print the full response for debugging
        
        # Ensure correct access to the content
        if response.choices and len(response.choices) > 0 and response.choices[0].message:
            return response.choices[0].message.content.strip()
        else:
            return "No valid response from AI"

    except Exception as e:  # If a problem occurs (for example, the internet is down), return the error message.
        return f"Error: {str(e)}"
    

if __name__ == "__main__":
    user_input = input("You: ")
    mood = input("Choose mood (default / sarcastic / enthusiastic / serious): ")
    response = get_ai_response(user_input, mood)
    print("AI:", response)
