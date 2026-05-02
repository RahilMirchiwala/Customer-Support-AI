import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()
client = Groq(api_key = os.getenv("GROQ_API_KEY"))

history = []

def generate_response(message: str, category: str, priority: str) -> str:
  system_prompt = f"""You are a helpful customer support agent.
    Category: {category}
    Priority: {priority}

    Rules:
    - If High priority: respond urgently and empathetically
    - If Billing: focus on payment solutions
    - If Technical: give clear troubleshooting steps
    - If General: give simple and informative answer 
    - Always be polite and professional"""
  
  # history.append({"role": "user", "content": message})

  messages=[
          {"role": "system", "content": system_prompt},
          *history,
          {"role": "user", "content": message}
      ]

  chat_completion = client.chat.completions.create(
    model="llama-3.3-70b-versatile",
    messages= messages
  )

  reply = chat_completion.choices[0].message.content

  history.append({"role": "user", "content": message})
  history.append({"role": "assistant", "content": reply})

  return reply