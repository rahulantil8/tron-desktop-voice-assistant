# ai.py
import os
from voice import speak

try:
    from openai import OpenAI
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    AI_AVAILABLE = True
except Exception:
    AI_AVAILABLE = False


def ask_ai(prompt: str):
    if not AI_AVAILABLE:
        speak("AI is not configured yet.")
        return

    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are Tron, a helpful desktop assistant."},
                {"role": "user", "content": prompt}
            ]
        )
        reply = response.choices[0].message.content
        speak(reply)
        return reply
    except Exception as e:
        print("[TRON AI ERROR]", e)
        speak("Sorry, I couldn't reach the AI.")
