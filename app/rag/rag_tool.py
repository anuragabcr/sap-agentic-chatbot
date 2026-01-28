from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

embeddings = OpenAIEmbeddings()
vectorstore = FAISS.load_local(
    os.path.join(BASE_DIR, "faiss_index"),
    embeddings,
    allow_dangerous_deserialization=True
)

retriever = vectorstore.as_retriever(search_kwargs={"k": 3})

def sap_rag_tool(query: str):
    """Retrieve SAP documentation and policy knowledge"""
    docs = retriever.get_relevant_documents(query)
    return "\n".join([d.page_content for d in docs])
