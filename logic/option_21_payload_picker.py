import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from core.payload_loader import get_payloads_by_category
from core.database import get_db_connection

def auto_pick_payload(category):
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT p.payload, COUNT(fr.id) as success_hits
        FROM payloads p
        LEFT JOIN fuzz_results fr ON p.payload = fr.payload AND fr.success = 1
        WHERE p.category = ?
        GROUP BY p.payload
        ORDER BY success_hits DESC
        LIMIT 1
    """, (category,))
    
    row = cursor.fetchone()
    conn.close()

    if row:
        return row[0]
    else:
        return None

# Automatski izbor (primer: 'XSS')
category = 'XSS'
chosen_payload = auto_pick_payload(category)

if chosen_payload:
    print(f"[🤖] Automatski izabran payload za kategoriju '{category}':\n{chosen_payload}")
else:
    print(f"[⚠️] Nema payload-a sa uspešnim rezultatima za kategoriju '{category}'")
