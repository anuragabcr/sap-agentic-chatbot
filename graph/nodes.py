from app.rag.rag_tool import sap_rag_tool
from app.tools.sql_agent import sql_agent
from app.sap_agent.tools.sap_tools import (
    check_sod_conflict_tool,
    create_access_request_tool,
)

# ---- RAG Node ----
def rag_node(state):
    answer = sap_rag_tool(state["query"])
    return {"response": answer}

# ---- SQL Node ----
def sql_node(state):
    result = sql_agent.invoke(state["query"])
    return {"response": result["output"]}

# ---- SAP Action Node ----
def sap_node(state):
    query = state["query"].lower()

    if "sod" in query:
        roles = ["Z_FI_AP_CLERK", "Z_FI_AP_APPROVER"]
        result = check_sod_conflict_tool(roles)
        return {"response": f"SoD conflicts: {result}"}

    if "create" in query or "request" in query:
        result = create_access_request_tool("ANURAG", "Z_MM_USER")
        return {"response": str(result)}

    return {"response": "SAP action not recognized"}
