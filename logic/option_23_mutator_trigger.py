# logic/option_23_mutator_trigger.py
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import sqlite3
import random
from datetime import datetime
from core.database import get_db_connection
MUTATION_TYPES = {
    "reverse": lambda p: p[::-1],
    "uppercase": lambda p: p.upper(),
    "append_junk": lambda p: p + "XYZ123",
    "insert_null": lambda p: p.replace("=", "=null;"),
    "obfuscate": lambda p: p.replace("<", "&lt;").replace(">", "&gt;"),
}

def get_recent_payloads(limit=5):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id, payload FROM fuzz_results ORDER BY timestamp DESC LIMIT ?", (limit,))
    data = cursor.fetchall()
    conn.close()
    return data

def insert_mutation(original_id, mutated, mutation_type):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO mutations (original_id, mutated_payload, mutation_type, created_at)
        VALUES (?, ?, ?, ?)
    """, (original_id, mutated, mutation_type, datetime.now().isoformat()))
    conn.commit()
    conn.close()

def mutate_payloads():
    payloads = get_recent_payloads()
    if not payloads:
        print("[yellow]Nema dostupnih payload-a za mutaciju.[/yellow]")
        return
    for original_id, payload in payloads:
        for mtype, func in MUTATION_TYPES.items():
            mutated = func(payload)
            insert_mutation(original_id, mutated, mtype)
            print(f"[green]Mutacija uspešna:[/green] {mutated} ⮕ [italic]{mtype}[/italic]")

if __name__ == "__main__":
    mutate_payloads()
