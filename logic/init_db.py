import sqlite3

def init_db():
    conn = sqlite3.connect("data/shadowfox.db")
    cursor = conn.cursor()

    # Tabela za fuzz rezultate (ulaz za mutator)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS fuzz_results (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            target TEXT,
            payload TEXT,
            response TEXT,
            status_code INTEGER,
            created_at TEXT
        )
    """)

    # Tabela za mutacije
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS mutations (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            fid INTEGER,
            target TEXT,
            original_payload TEXT,
            mutated_payload TEXT,
            hash_id TEXT UNIQUE,
            created_at TEXT
        )
    """)

    conn.commit()
    conn.close()
    print("[✓] Baza inicijalizovana.")

if __name__ == "__main__":
    init_db()
