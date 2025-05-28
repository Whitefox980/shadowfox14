import sqlite3
import time
from datetime import datetime

REQUIRED_TABLES = [
    "targets", "payloads", "fuzz_results", "mutations",
    "scan_logs", "agent_activity", "operator_log", "operator_errors"
]

def watchdog_loop():
    while True:
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        conn = sqlite3.connect("shadowfox.db")
        cursor = conn.cursor()

        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        existing_tables = {row[0] for row in cursor.fetchall()}

        for table in REQUIRED_TABLES:
            if table not in existing_tables:
                cursor.execute("""
                    INSERT INTO operator_errors (timestamp, missing_table)
                    VALUES (?, ?)
                """, (now, table))
                print(f"[!] Nedostaje tabela: {table} → logovano u operator_errors.")

        conn.commit()
        conn.close()
        time.sleep(15)  # svakih 15 sekundi proverava

if __name__ == "__main__":
    watchdog_loop()
