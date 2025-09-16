
from langchain_ollama import OllamaEmbeddings
from langchain_chroma import Chroma
from langchain_core.documents import Document
import os
import pandas as pand

df = pand.read_csv("Store_reviews.csv")

embeddings = OllamaEmbeddings(model="mxbai-embed-large")

db_location = "./chroma_langchain_db"

add_documents = not os.path.exists(db_location)

vector_store = Chroma(
    collection_name="restaurant_reviews",
    persist_directory=db_location,
    embedding_function=embeddings
)

if add_documents:
    print("Creating new vector database and adding documents...")
    documents = []
    ids = []
    
    for i, row in df.iterrows():
        page_content = str(row["Title"]) + " " + str(row["Review"])
        
        document = Document(
            page_content=page_content,
            metadata={"rating": row["Rating"], "date": row["Date"]},
        )
        ids.append(str(i))
        documents.append(document)
        
    vector_store.add_documents(documents=documents, ids=ids)
    print("Documents added successfully.")

retriever = vector_store.as_retriever(
    search_kwargs={"k": 5} 
)

print("Retriever is ready.")
