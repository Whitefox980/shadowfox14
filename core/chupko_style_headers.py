import sqlite3
import requests
from datetime import datetime

DB_PATH = "data/shadowfox.db"

def run_chupko_headers():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    try:
        cursor.execute("SELECT target, payload FROM validated_hits")
        hits = cursor.fetchall()

        if not hits:
            print("[!] Nema validiranih pogodaka za branding fazu.")
            return

        print(f"[+] Branding faza za {len(hits)} meta...")

        headers = {
            "X-Chupko-Flag": "Chupko was here 🐺",
            "X-H1-Agent": "Whitefox980",
            "User-Agent": "Mozilla/5.0 (WhiteFoxAgent/13.37)"
        }

        for target, payload in hits:
            url = f"{target}?input={payload}"
            try:
                r = requests.get(url, headers=headers, timeout=8)
                if r.status_code in [200, 302]:
                    print(f"[✓] Branding uspešan → {url}")
                    cursor.execute("""
                        INSERT INTO chupko_log (target, payload, response_code, timestamp)
                        VALUES (?, ?, ?, ?)
                    """, (target, payload, r.status_code, datetime.now()))
            except Exception as e:
                print(f"[✗] Greška za {url}: {e}")

        conn.commit()

    except Exception as ex:
        print(f"[!] Greška u branding fazi: {ex}")
    finally:
        conn.close()

if __name__ == "__main__":
    run_chupko_headers()
