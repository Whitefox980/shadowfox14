import sqlite3
from core.agent_logger import log_agent_activity

def recon_scan():
    conn = sqlite3.connect("shadowfox.db")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS targets (id INTEGER PRIMARY KEY AUTOINCREMENT, url TEXT)")
    cursor.execute("SELECT url FROM targets")
    targets = cursor.fetchall()
    conn.close()

    for target in targets:
        url = target[0]
        print(f"[RECON] Skeniram metu: {url}")
        log_agent_activity("ReconAgent", "scanned", url)

if __name__ == "__main__":
    recon_scan()
