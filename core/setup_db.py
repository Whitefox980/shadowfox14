import sqlite3

DB_PATH = "data/shadowfox.db"

def create_tables():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()

    # Tabela za mete
    c.execute('''CREATE TABLE IF NOT EXISTS targets (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        url TEXT NOT NULL,
        description TEXT
    )''')

    # Tabela za osnovne fuzz rezultate
    c.execute('''CREATE TABLE IF NOT EXISTS fuzz_results (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        target TEXT,
        payload TEXT,
        module TEXT,
        response TEXT,
        success INTEGER DEFAULT 0,
        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
    )''')

    # Tabela za mutacije
    c.execute('''CREATE TABLE IF NOT EXISTS mutations (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        original_payload TEXT,
        mutated_payload TEXT,
        technique TEXT,
        quality_score REAL,
        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
    )''')

    # Tabela za AI analizu
    c.execute('''CREATE TABLE IF NOT EXISTS ai_analysis (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        payload TEXT,
        analysis TEXT,
        severity TEXT,
        ai_model TEXT,
        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
    )''')

    # Tabela za napade (executed payloads)
    c.execute('''CREATE TABLE IF NOT EXISTS attack_log (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        target TEXT,
        payload TEXT,
        result TEXT,
        proof_file TEXT,
        status TEXT,
        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
    )''')

    # Tabela za operatereve intervencije
    c.execute('''CREATE TABLE IF NOT EXISTS operator_log (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        action TEXT,
        detail TEXT,
        source_module TEXT,
        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
    )''')

    conn.commit()
    conn.close()
    print("[✓] Baza i sve tabele uspešno kreirane.")

if __name__ == "__main__":
    create_tables()
