import sqlite3
from datetime import datetime

def log_agent_activity(agent_name, action, target):
    conn = sqlite3.connect("shadowfox.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS agent_activity (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp TEXT,
            agent_name TEXT,
            action TEXT,
            target TEXT
        )
    """)
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    cursor.execute("INSERT INTO agent_activity (timestamp, agent_name, action, target) VALUES (?, ?, ?, ?)",
                   (timestamp, agent_name, action, target))
    conn.commit()
    conn.close()
