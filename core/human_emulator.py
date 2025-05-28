import random
import time
from database import get_db_connection
from utils.user_agents import get_random_user_agent

def simulate_human_behavior(target_url):
    conn = get_db_connection()
    cursor = conn.cursor()

    headers = {
        "User-Agent": get_random_user_agent(),
        "Accept-Language": "en-US,en;q=0.9",
        "Connection": "keep-alive"
    }

    paths = ["/home", "/login", "/search", "/products", "/about"]
    clicks = random.randint(2, 5)

    print(f"[🧠] Simulating human behavior on: {target_url}")
    session_payload = ""

    for _ in range(clicks):
        path = random.choice(paths)
        full_url = f"{target_url.rstrip('/')}/{path.lstrip('/')}"
        print(f"[→] Visiting: {full_url}")
        time.sleep(random.uniform(0.7, 1.9))

        if random.random() < 0.3:
            session_payload = "<script>alert('Chupko was here')</script>"
            print(f"[⚡] Injecting payload at: {full_url}")

            cursor.execute("""
                INSERT INTO human_emulator_logs (target, payload, response, timestamp)
                VALUES (?, ?, ?, datetime('now'))
            """, (full_url, session_payload, "Simulated click inject",))

            conn.commit()

    print(f"[✓] Simulation completed for {target_url}")
    conn.close()

if __name__ == "__main__":
    target = input("Unesi URL mete: ").strip()
    simulate_human_behavior(target)
