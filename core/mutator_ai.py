# core/mutator_ai.py

import sqlite3
import random
from datetime import datetime

DB_PATH = "shadowfox.db"

MUTATION_TYPES = [
    "prefix_injection", "suffix_injection", "double_encoding",
    "case_flipping", "comment_injection", "null_byte"
]

def get_successful_payloads():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT id, payload FROM fuzz_results WHERE success = 1")
    results = cursor.fetchall()
    conn.close()
    return results

def mutate_payload(payload, mutation_type):
    if mutation_type == "prefix_injection":
        return "pre_" + payload
    elif mutation_type == "suffix_injection":
        return payload + "_suf"
    elif mutation_type == "double_encoding":
        return payload.replace("<", "%3C").replace(">", "%3E")
    elif mutation_type == "case_flipping":
        return ''.join([c.upper() if i % 2 == 0 else c.lower() for i, c in enumerate(payload)])
    elif mutation_type == "comment_injection":
        return payload + "/**/"
    elif mutation_type == "null_byte":
        return payload + "%00"
    return payload

def save_mutation(original_id, mutated_payload, mutation_type):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO mutations (original_id, mutated_payload, mutation_type, created_at)
        VALUES (?, ?, ?, ?)
    """, (original_id, mutated_payload, mutation_type, datetime.now().isoformat()))
    conn.commit()
    conn.close()

def run_mutator():
    payloads = get_successful_payloads()
    if not payloads:
        print("[⚠️] Nema uspešnih payload-a za mutaciju.")
        return

    for original_id, payload in payloads:
        for mutation_type in MUTATION_TYPES:
            mutated = mutate_payload(payload, mutation_type)
            save_mutation(original_id, mutated, mutation_type)
            print(f"[+] Mutacija: {mutation_type} → {mutated}")

if __name__ == "__main__":
    run_mutator()
