import os
from groq import Groq
from dotenv import load_dotenv
from retriever import search

load_dotenv()
client = Groq(api_key = os.getenv("GROQ_API_KEY"))

history = []

def generate_response(message: str, category: str, priority: str, context: str = "") -> str:

  relevent_chunks = search(message)
  context = "\n".join([chunk.page_content for chunk in relevent_chunks])  

  system_prompt = f"""You are a helpful customer support agent.
    Category: {category}
    Priority: {priority}

    Use this knowledge base to answer:
    {context} 
    
    Rules:
    - Answer based on the context above
    - If not in context, say "I don't have info on this"
    - If High priority: respond urgently and empathetically
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