# Customer Support AI

AI-powered customer support system that classifies 
messages and generates responses automatically.

## What it does
- Classifies messages: Billing / Technical / General
- Detects priority: High / Medium / Low
- Generates AI response using Groq + Llama 3.3
- Remembers conversation context (memory)

## Tech Stack
Python, FastAPI, Groq API, Pydantic

## Run locally
pip install -r requirements.txt
uvicorn main:app --reload
