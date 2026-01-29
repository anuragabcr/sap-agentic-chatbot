from langgraph.graph import StateGraph, END
from graph.state import AgentState
from graph.router import route_intent
from graph.nodes import rag_node, sql_node, sap_node


graph = StateGraph(AgentState)

# Nodes
graph.add_node("router", route_intent)
graph.add_node("rag", rag_node)
graph.add_node("sql", sql_node)
graph.add_node("sap", sap_node)

# Entry
graph.set_entry_point("router")

# Conditional routing
graph.add_conditional_edges(
    "router",
    lambda state: state["intent"],
    {
        "RAG": "rag",
        "SQL": "sql",
        "SAP": "sap",
    }
)

# End all paths
graph.add_edge("rag", END)
graph.add_edge("sql", END)
graph.add_edge("sap", END)

agent = graph.compile()
