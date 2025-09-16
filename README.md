Using RAG (Retrieval-Augmented Generation) with LangChain + Ollama + Chroma, 
I built a prototype that embeds restaurant reviews into a vector database and enables natural language Q&A on top of them.


How it works:
- Reviews are embedded into vectors and stored in Chroma.
- A retriever fetches the most relevant ones.
- A LLM (Llama 3 via Ollama) answers the user’s question, grounded in actual reviews.
