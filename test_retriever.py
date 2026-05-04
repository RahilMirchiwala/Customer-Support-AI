from ingestor import load_and_split
from retriever import store_chunks, search

chunks = load_and_split("customer_support_faq.pdf")
print(f"Chunks loaded: {len(chunks)}")

store_chunks(chunks)
print("Stored in ChromaDB!")

results = search("refund policy")
for r in results:
    print(r.page_content)
    print("---")