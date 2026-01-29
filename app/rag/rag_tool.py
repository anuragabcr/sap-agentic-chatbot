import os
from langchain_community.vectorstores import FAISS

# ---- Embedding selection (safe) ----
def get_embeddings():
    from langchain_huggingface import HuggingFaceEmbeddings
    return HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

# ---- Load FAISS index lazily ----
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
_FAISS = None

def get_vectorstore():
    global _FAISS
    if _FAISS is None:
        embeddings = get_embeddings()
        _FAISS = FAISS.load_local(
            os.path.join(BASE_DIR, "faiss_index"),
            embeddings,
            allow_dangerous_deserialization=True
        )
    return _FAISS

# def sap_rag_tool(query: str):
#     """Retrieve SAP documentation and policy knowledge"""
#     vectorstore = get_vectorstore()
#     retriever = vectorstore.as_retriever(search_kwargs={"k": 3})
#     docs = retriever.invoke(query)
#     return "\n".join(d.page_content for d in docs)


from app.llm.openrouter_client import call_gemma

def sap_rag_tool(query: str):
    vectorstore = get_vectorstore()
    retriever = vectorstore.as_retriever(search_kwargs={"k": 3})
    docs = retriever.invoke(query)

    context = "\n\n".join(d.page_content for d in docs)

    prompt = f"""
        You are an SAP assistant.
        Answer the question using ONLY the context below.
        If the answer is not present, say "I don't know".

        Context:
        {context}

        Question:
        {query}

        Answer in 1–2 sentences:
        """

    return call_gemma(prompt)
