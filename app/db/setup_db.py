import sqlite3
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, "sap.db")

conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS AGR_USERS (
    UNAME TEXT,
    AGR_NAME TEXT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS AGR_TCODES (
    AGR_NAME TEXT,
    TCODE TEXT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS TSTC (
    TCODE TEXT,
    TTEXT TEXT
)
""")

cursor.executemany(
    "INSERT INTO AGR_USERS VALUES (?, ?)",
    [
        ("ANURAG", "Z_MM_USER"),
        ("ANURAG", "Z_FI_CLERK"),
        ("JOHN", "Z_SD_USER")
    ]
)

cursor.executemany(
    "INSERT INTO AGR_TCODES VALUES (?, ?)",
    [
        ("Z_MM_USER", "ME23N"),
        ("Z_MM_USER", "ME21N"),
        ("Z_FI_CLERK", "FB60")
    ]
)

cursor.executemany(
    "INSERT INTO TSTC VALUES (?, ?)",
    [
        ("ME23N", "Display Purchase Order"),
        ("ME21N", "Create Purchase Order"),
        ("FB60", "Enter Vendor Invoice")
    ]
)

conn.commit()
conn.close()

print(f"✅ SAP database created at: {DB_PATH}")
