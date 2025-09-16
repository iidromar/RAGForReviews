from langchain_ollama.llms import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
from vector import retriever

model = OllamaLLM(model="llama3.2")

template = """
You are an exeprt in answering questions about a specific store/restaurant

Here are some relevant reviews: {reviews}

Here is the question to answer: {question}

If you didn't find any review similar to the question, answer the question by saying: Sorry, there are no reviews mentioned this information.
Don't answer any religion, politics or any not related questions.
"""
prompt = ChatPromptTemplate.from_template(template)
chain = prompt | model

while True:
    question = input("Ask your question or type q to quit: ")
    if question == "q":
        break
    
    reviews = retriever.invoke(question)
    result = chain.invoke({"reviews": reviews, "question": question})
    print(result)