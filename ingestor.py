# Document Processing
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

def load_and_split(file_path: str):
  loader = PyPDFLoader(file_path)
  documents = loader.load()

  splitter = RecursiveCharacterTextSplitter(
    chunk_size = 500,
    chunk_overlap = 50
  )

  chunks = splitter.split_documents(documents)

  return chunks

# Test
'''
chunks = load_and_split("customer_support_faq.pdf")
print(f"Total chunks: {len(chunks)}")
print(chunks[0].page_content)
''' 