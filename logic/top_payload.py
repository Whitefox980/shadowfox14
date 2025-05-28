# logic/top_payload.py

import sqlite3
from rich.console import Console
from rich.table import Table

def show_top_payload():
    conn = sqlite3.connect("shadowfox.db")
    c = conn.cursor()

    c.execute("""
        SELECT payload, COUNT(*) as hits
        FROM fuzz_results
        WHERE success = 1
        GROUP BY payload
        ORDER BY hits DESC
        LIMIT 5
    """)
    results = c.fetchall()
    conn.close()

    console = Console()
    table = Table(title="🔥 Top 5 Najuspešnijih Payloada", show_lines=True)
    table.add_column("Payload", style="yellow")
    table.add_column("Uspešni Pogoci", style="green")

    for payload, hits in results:
        table.add_row(payload, str(hits))

    console.print(table)

if __name__ == "__main__":
    show_top_payload()
