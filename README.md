# Customer Support AI 🤖
AI-powered customer support system that classifies 
messages, searches a knowledge base, and generates responses.

## Live Demo
🌐 https://customer-support-ai-97ym.onrender.com

## What it does
- Classifies messages: Billing / Technical / General
- Detects priority: High / Medium / Low
- Searches FAQ knowledge base using RAG + ChromaDB
- Generates AI response using Groq + Llama 3.3
- Conversation memory across messages

## Tech Stack
- Python
- FastAPI
- Groq API (Llama 3.3 70B)
- LangChain + ChromaDB (RAG)
- HuggingFace Embeddings
- Pydantic

## API Endpoints
- `GET  /`    → UI
- `POST /ask` → Classify + Search + Generate Response
- `GET  /docs` → API Documentation

## Run Locally
git clone https://github.com/RahilMirchiwala/Customer-Support-AI
cd Customer-Support-AI
pip install -r requirements.txt
uvicorn main:app --reload

## Environment Variables
GROQ_API_KEY=your_key_here
