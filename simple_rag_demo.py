# Simple RAG Prototype
# This is a mock-up of my current RAG approach
import numpy as np

def mock_vector_search(query, documents):
    print(f"Searching for: {query}...")
    # Simulating vector similarity search
    return documents[0] 

docs = ["AMD GPUs provide great performance for ROCm", "LLMs are changing the world"]
result = mock_vector_search("AMD GPU performance", docs)
print(f"Found relevant context: {result}")
