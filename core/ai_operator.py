import sqlite3
from datetime import datetime

REQUIRED_TABLES = [
    "targets", "payloads", "fuzz_results", "mutations",
    "scan_logs", "agent_activity", "operator_log"
]

def scan_modules():
    conn = sqlite3.connect('shadowfox.db')
    cursor = conn.cursor()

    # Detekcija svih tabele u bazi
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
    existing_tables = [row[0] for row in cursor.fetchall()]

    print(f"\n[AI OPERATOR] Detektovane tabele ({len(existing_tables)}):")
    for t in existing_tables:
        print(f" - {t}")

    # Log detekcije u operator_log
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS operator_log (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp TEXT,
            module TEXT
        )
    """)
    for t in existing_tables:
        cursor.execute("INSERT INTO operator_log (timestamp, module) VALUES (?, ?)", (now, t))

    # Provera da li postoje sve obavezne tabele
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS operator_errors (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp TEXT,
            missing_table TEXT
        )
    """)
    for req in REQUIRED_TABLES:
        if req not in existing_tables:
            print(f"[!] NEDOSTAJE TABELA: {req}")
            cursor.execute("INSERT INTO operator_errors (timestamp, missing_table) VALUES (?, ?)", (now, req))

    conn.commit()
    conn.close()

if __name__ == "__main__":
    scan_modules()
