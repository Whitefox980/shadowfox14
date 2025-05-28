import sqlite3

def init_tables():
    conn = sqlite3.connect("shadowfox.db")
    cursor = conn.cursor()

    cursor.execute("""CREATE TABLE IF NOT EXISTS targets (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        url TEXT,
        source TEXT,
        timestamp TEXT
    )""")

    cursor.execute("""CREATE TABLE IF NOT EXISTS payloads (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        payload TEXT,
        category TEXT,
        description TEXT,
        origin TEXT,
        timestamp TEXT
    )""")

    cursor.execute("""CREATE TABLE IF NOT EXISTS fuzz_results (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        target TEXT,
        payload TEXT,
        category TEXT,
        status TEXT,
        response TEXT,
        severity INTEGER,
        timestamp TEXT
    )""")

    cursor.execute("""CREATE TABLE IF NOT EXISTS mutations (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        original_payload TEXT,
        mutated_payload TEXT,
        logic TEXT,
        status TEXT,
        timestamp TEXT
    )""")

    cursor.execute("""CREATE TABLE IF NOT EXISTS scan_logs (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        agent TEXT,
        target TEXT,
        module TEXT,
        payload TEXT,
        result TEXT,
        timestamp TEXT
    )""")

    cursor.execute("""CREATE TABLE IF NOT EXISTS agent_activity (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        agent_name TEXT,
        action TEXT,
        target TEXT,
        status TEXT,
        timestamp TEXT
    )""")

    cursor.execute("""CREATE TABLE IF NOT EXISTS operator_log (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        action TEXT,
        origin TEXT,
        status TEXT,
        timestamp TEXT
    )""")

    cursor.execute("""CREATE TABLE IF NOT EXISTS operator_errors (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        timestamp TEXT,
        missing_table TEXT
    )""")

    conn.commit()
    conn.close()
    print("[✓] Sve ShadowFox tabele su kreirane.")

if __name__ == "__main__":
    init_tables()
