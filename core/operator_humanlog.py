
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import time
from core.database import get_db_connection
from rich.console import Console
from rich.table import Table
import sqlite3
import os
import time
from core.database import get_db_connection

def log_human_event(event_type, target_url, notes):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO human_behavior_log (timestamp, event_type, target_url, notes)
        VALUES (?, ?, ?, ?)
    """, (int(time.time()), event_type, target_url, notes))
    conn.commit()
    conn.close()
    print(f"[+] Zabeleženo: {event_type} → {target_url}")

# Test primer
console = Console()

def fetch_latest_logs(limit=10):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT target, payload, response, timestamp
        FROM human_emulator_logs
        ORDER BY timestamp DESC
        LIMIT ?
    """, (limit,))
    results = cursor.fetchall()
    conn.close()
    return results

def display_logs():
    while True:
        logs = fetch_latest_logs()
        table = Table(title="📍 Human Emulator Logovi", expand=True)

        table.add_column("Vreme", style="cyan", no_wrap=True)
        table.add_column("Meta", style="magenta")
        table.add_column("Payload", style="yellow")
        table.add_column("Odgovor", style="green")

        for log in logs:
            target, payload, response, timestamp = log
            table.add_row(timestamp, target, payload or "-", response or "-")

        console.clear()
        console.print(table)
        time.sleep(5)

if __name__ == "__main__":
    log_human_event("mouse_move", "https://example.com", "korisnik se kretao normalno")
    display_logs()
