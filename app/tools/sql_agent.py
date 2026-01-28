from langchain_community.utilities import SQLDatabase
from langchain_community.agent_toolkits import SQLDatabaseToolkit
from langchain_openai import ChatOpenAI
from langchain.agents import create_sql_agent

from db.db_connection import engine

llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0
)

db = SQLDatabase(engine)

sql_toolkit = SQLDatabaseToolkit(
    db=db,
    llm=llm
)

sql_tools = sql_toolkit.get_tools()

sql_agent = create_sql_agent(
    llm=llm,
    toolkit=sql_toolkit,
    verbose=True
)