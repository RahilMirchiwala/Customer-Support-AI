from fastapi import FastAPI, File, UploadFile
from models import SupportTicket, SupportResponse
from classifier import classify_message,detect_priority
from chat import generate_response
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from ingestor import load_and_split
from retriever import search,store_chunks
from contextlib import asynccontextmanager

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Server start hote hi FAQ load karo
    chunks = load_and_split("customer_support_faq.pdf")
    store_chunks(chunks)
    print("FAQ loaded into ChromaDB!")
    yield

app = FastAPI(lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def serve_ui():
    return FileResponse("chatbox.html")

@app.post("/ask")
async def ask_question(ticket: SupportTicket):

  results = search(ticket.message)
  context = "\n".join([r.page_content for r in results])

  category = classify_message(ticket.message)
  priority = detect_priority(ticket.message)

  response = generate_response(ticket.message, category, priority, context)

  return SupportResponse(
    category=category,
    priority=priority,
    response=response
  )