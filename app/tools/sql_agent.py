from sqlalchemy import text
from app.db.db_connection import engine

class MockSQLAgent:
    def invoke(self, query: str):
        q = query.lower()

        if "t-code" in q or "tcode" in q:
            sql = """
            SELECT TCODE FROM AGR_TCODES
            WHERE AGR_NAME = 'Z_MM_USER'
            """
        elif "role" in q and "anurag" in q:
            sql = """
            SELECT AGR_NAME FROM AGR_USERS
            WHERE UNAME = 'ANURAG'
            """
        else:
            return {"output": "Query not supported"}

        with engine.connect() as conn:
            rows = conn.execute(text(sql)).fetchall()

        return {
            "output": ", ".join(r[0] for r in rows)
        }

sql_agent = MockSQLAgent()
