from .sql_agent import sql_agent

response = sql_agent.invoke(
    "What T-codes are assigned to role Z_MM_USER?"
)

print(response)
