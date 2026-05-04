# ChormaDB Search
from langchain_community.vectorstores import Chroma
from langchain_huggingface import HuggingFaceEmbeddings

embedding_model = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-mpnet-base-v2"
)
db = None

def store_chunks(chunks):
  global db
  db = Chroma.from_documents(
    documents=chunks,
    embedding=embedding_model
  )

def search(query: str):
  results = db.similarity_search(query, k = 3)
  return results