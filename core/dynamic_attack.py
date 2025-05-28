from core.payload_loader import get_payloads_by_category
from core.database import get_db_connection
import requests

def attack_with_payloads(category):
    payloads = get_payloads_by_category(category)
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT url FROM targets")
    targets = [row[0] for row in cursor.fetchall()]
    conn.close()

    for target in targets:
        for payload in payloads:
            try:
                url = f"{target}?input={payload}"
                r = requests.get(url, timeout=6)
                print(f"[✓] {target} <= {payload} | Status: {r.status_code}")
            except Exception as e:
                print(f"[!] Greška za {target} | {e}")

if __name__ == "__main__":
    attack_with_payloads("XSS")  # Primer - koristi XSS
