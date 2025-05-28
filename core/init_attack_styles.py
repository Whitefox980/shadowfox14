import sqlite3

def init_attack_styles():
    conn = sqlite3.connect("core/shadowfox.db")
    c = conn.cursor()

    c.execute("""
        CREATE TABLE IF NOT EXISTS attack_styles (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            user_agent TEXT,
            headers TEXT,
            speed TEXT,
            mode TEXT,
            note TEXT,
            created_at DATETIME DEFAULT CURRENT_TIMESTAMP
        );
    """)

    conn.commit()
    conn.close()
    print("[✓] Tabela 'attack_styles' uspešno kreirana.")

if __name__ == "__main__":
    init_attack_styles()
