
# 🧠 `ai_engine.md`

## Overview

This module (`ai_engine.py`) handles all communication between the chatbot and the AI model via the OpenRouter API. It allows the chatbot to send user prompts, customize responses based on mood, and fetch AI-generated replies.

---

## 🔧 Dependencies

```python
import os
from dotenv import load_dotenv
from openai import OpenAI
```

* `os`: Used to access environment variables (e.g., the API key).
* `dotenv`: Loads sensitive values like `OPENROUTER_API_KEY` from a `.env` file, keeping credentials out of the code.
* `OpenAI`: The OpenRouter-compatible client library that sends requests to the chosen AI model.

---

## 🌐 Environment Setup

```python
load_dotenv()
api_key = os.getenv("OPENROUTER_API_KEY")
```

* Loads the `.env` file.
* Extracts the `OPENROUTER_API_KEY` and stores it for authentication.

---

## 🤖 AI Client Setup

```python
client = OpenAI(
    api_key=api_key,
    base_url="https://openrouter.ai/api/v1"
)
```

* Instantiates the OpenAI client using the API key and the base URL for OpenRouter.

---

## ✨ Prompt Creation

```python
def create_prompt(user_input, mood="default"):
```

This function modifies the user’s input based on the selected **mood**. It adjusts tone and context before sending it to the AI.

Supported moods:

* **sarcastic** – Adds wit and snark.
* **enthusiastic** – Boosts positivity and hype.
* **serious** – Adds formality and focus.
* **default** – Sends input as-is.

---

## 🎭 Mood Selection

```python
def ask_for_mood():
```

Prompts the user to choose their desired mood via terminal input. This helps tailor the chatbot’s personality on demand.

---

## 🧠 AI Response Handler

```python
def get_ai_response(user_input, mood="default"):
```

Handles the full AI interaction flow:

1. Builds the prompt via `create_prompt`.
2. Sends the prompt to the Mistral 7B model via OpenRouter.
3. Configures:

   * `max_tokens`: Max reply length (150 tokens).
   * `temperature`: Controls randomness (0.7 = balanced).
4. Returns a clean text response from the AI, or an error message if the request fails.

---

## 🧪 Main Execution Block

```python
if __name__ == "__main__":
```

This block allows the module to run independently for testing:

* Takes user input and mood from the terminal.
* Calls `get_ai_response()`.
* Prints the AI’s reply.

---

## 📌 Notes

* The AI model used is: `"mistralai/mistral-7b-instruct"` — a lightweight, efficient instruction-tuned LLM.
* `response.choices[0].message.content` is accessed cautiously to prevent errors in case the response structure changes or fails.

---

## ✅ Example Usage

```bash
You: What’s the meaning of life?
Choose mood (default / sarcastic / enthusiastic / serious): sarcastic
AI: Oh, just 42. Obviously. Duh.
```

---
