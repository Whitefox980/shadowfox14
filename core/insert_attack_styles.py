import sqlite3

def insert_default_styles():
    conn = sqlite3.connect("core/shadowfox.db")
    c = conn.cursor()

    styles = [
        ("Stealth", "Mozilla/5.0 (Windows NT 10.0; Win64; x64)", '{"X-Requested-With": "XMLHttpRequest"}', "slow", "human", "Diskretan napad sa niskim intenzitetom."),
        ("Aggressive", "sqlmap/1.5.2", '{"X-Attack": "Yes"}', "fast", "bruteforce", "Brzi napad sa svim payloadima."),
        ("Custom", "", "{}", "medium", "manual", "Stil za ručno podešavanje.")
    ]

    c.executemany("""
        INSERT INTO attack_styles (name, user_agent, headers, speed, mode, note)
        VALUES (?, ?, ?, ?, ?, ?)
    """, styles)

    conn.commit()
    conn.close()
    print("[✓] Ubaceni osnovni stilovi napada u tabelu.")

if __name__ == "__main__":
    insert_default_styles()
