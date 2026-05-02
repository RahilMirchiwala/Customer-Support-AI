from fastapi import FastAPI
from models import SupportTicket, SupportResponse
from classifier import classify_message,detect_priority
from chat import generate_response
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/support", response_model=SupportResponse)
async def handle_support(ticket:SupportTicket):
  category = classify_message(ticket.message)
  priority = detect_priority(ticket.message)
  response = generate_response(ticket.message,category,priority)

  return SupportResponse(
    category=category,
    priority=priority,
    response=response
  )