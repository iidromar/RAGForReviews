
from langchain_ollama.llms import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.documents import Document
from vector import retriever 

model = OllamaLLM(model="llama3")

template = """
You are an expert in answering questions about a specific store/restaurant based on the reviews provided.

Here are some relevant reviews:
{reviews}

Based only on the reviews above, answer the following question: {question}

If the reviews don't contain information to answer the question, you must say: "Sorry, there are no reviews that mention this information."
Do not answer any questions related to religion, politics, or other unrelated topics.
"""
prompt = ChatPromptTemplate.from_template(template)

chain = prompt | model

def get_response(question: str) -> tuple[str, list[Document]]:
    """
    Takes a user question, retrieves relevant reviews, and generates an answer.

    Args:
        question: The user's question.

    Returns:
        A tuple containing the generated answer (str) and the list of retrieved reviews (list[Document]).
    """
    reviews = retriever.invoke(question)
    
    answer = chain.invoke({"reviews": reviews, "question": question})
    
    return answer, reviews
