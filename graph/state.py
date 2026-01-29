from typing import TypedDict, Optional

class AgentState(TypedDict):
    query: str
    intent: Optional[str]
    response: Optional[str]
