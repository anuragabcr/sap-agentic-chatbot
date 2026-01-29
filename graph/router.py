from app.llm.openrouter_client import call_gemma

def route_intent(state):
    query = state["query"]

    prompt = f"""
You are an intent classifier for an SAP assistant.

Classify the user query into ONE category:
- RAG → SAP documentation, T-code meaning, how-to questions
- SQL → Queries about roles, users, T-codes from tables
- SAP → Actions like SoD check, create access request, request status

Query: "{query}"

Return only one word: RAG, SQL, or SAP.
"""

    intent = call_gemma(prompt).upper().strip()
    return {"intent": intent}
