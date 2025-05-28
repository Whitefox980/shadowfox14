import sqlite3
import requests
import time
from urllib.parse import urlparse

DB_PATH = "scan_results.db"
TARGETS_PATH = "data/targets.txt"
PAYLOADS_PATH = "data/payloads.txt"

def auto_evaluate_success(payload_id, response_code, reflected, response_size, baseline_size=500):
    if reflected == 1 and response_code == 200 and abs(response_size - baseline_size) > 50:
        conn = sqlite3.connect("shadowfox.db")
        cursor = conn.cursor()
        cursor.execute("UPDATE fuzz_results SET success = 1 WHERE id = ?", (payload_id,))
        conn.commit()
        conn.close()
def create_table():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS fuzz_results (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    target TEXT,
                    payload TEXT,
                    status_code INTEGER,
                    content_length INTEGER,
                    response TEXT,
                    timestamp TEXT
                )''')
    conn.commit()
    conn.close()

def load_targets():
    with open(TARGETS_PATH, "r") as f:
        return [line.strip() for line in f if line.strip()]

def load_payloads():
    with open(PAYLOADS_PATH, "r") as f:
        return [line.strip() for line in f if line.strip()]

def fuzz_target(target, payloads):
    results = []
    for payload in payloads:
        url = target.replace("FUZZ", payload)
        try:
            r = requests.get(url, timeout=10)
            result = {
                "target": target,
                "payload": payload,
                "status_code": r.status_code,
                "content_length": len(r.content),
                "response": r.text[:500],  # samo prvih 500 karaktera
                "timestamp": time.strftime("%Y-%m-%d %H:%M:%S")
            }
            results.append(result)
        except Exception as e:
            continue
    return results

def save_results(results):
    conn = sqlite3.connect("shadowfox.db")  # ispravno ime baze
    c = conn.cursor()
    for res in results:
        c.execute('''INSERT INTO fuzz_results 
                     (target, payload, response_code, response_size, reflected, success, timestamp) 
                     VALUES (?, ?, ?, ?, ?, ?, ?)''',
                  (res["target"], res["payload"], res["status_code"],
                   res["content_length"], 0, 0, res["timestamp"]))
        
        payload_id = c.lastrowid
        # ✨ Pozivamo evaluaciju odmah nakon unosa
        auto_evaluate_success(payload_id, res["status_code"], 0, res["content_length"])
    
    conn.commit()
    conn.close()
def main():
    print("[*] Pokrećem fuzzing...")
    create_table()
    targets = load_targets()
    payloads = load_payloads()

    for target in targets:
        if "FUZZ" not in target:
            print(f"[!] Meta {target} nema 'FUZZ' u sebi – preskačem.")
            continue
        print(f"[+] Fuzzujem: {target}")
        results = fuzz_target(target, payloads)
        save_results(results)
        print(f"    -> Sačuvano {len(results)} rezultata.")

if __name__ == "__main__":
    main()
