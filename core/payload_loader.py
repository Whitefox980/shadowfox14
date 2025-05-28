import sqlite3

def get_payloads_by_category(category):
    conn = sqlite3.connect("shadowfox.db")
    cursor = conn.cursor()
    cursor.execute("SELECT payload FROM payloads WHERE category = ?", (category,))
    results = [row[0] for row in cursor.fetchall()]
    conn.close()
    return results

# Primer testa
if __name__ == "__main__":
    xss_payloads = get_payloads_by_category("XSS")
    print("[XSS PAYLOADI]")
    for p in xss_payloads:
        print(p)
