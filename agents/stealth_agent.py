import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'core')))
from agent_logger import log_agent_activity
import time
import random
import sqlite3

def simulate_human_behavior(target_url, payload):
    print(f"[STEALTH] Pristupam sajtu kao korisnik: {target_url}")
    log_agent_activity("StealthAgent", "accessed", target_url)

    # 🧠 Simulacija ljudskih pokreta
    steps = ["scrolling", "clicking", "pausing", "hovering", "typing"]
    for i in range(random.randint(2, 5)):
        action = random.choice(steps)
        wait = random.uniform(1.5, 3.5)
        print(f"[STEALTH] {action} ... ({wait:.1f}s)")
        time.sleep(wait)

    # 🚀 Ispaljujemo pravi mutirani payload
    print(f"[STEALTH] Ubacujem payload: {payload}")
    log_agent_activity("StealthAgent", "payload_injected", f"{target_url} | {payload}")

def stealth_mission():
    conn = sqlite3.connect("shadowfox.db")
    cursor = conn.cursor()

    cursor.execute("SELECT url FROM targets")
    targets = [t[0] for t in cursor.fetchall()]

    cursor.execute("SELECT payload FROM mutations ORDER BY RANDOM() LIMIT 1")
    payload_row = cursor.fetchone()
    payload = payload_row[0] if payload_row else "<script>alert('mutacija')</script>"

    conn.close()

    for target in targets:
        simulate_human_behavior(target, payload)

if __name__ == "__main__":
    stealth_mission()
