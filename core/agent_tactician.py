import sqlite3
from collections import Counter

DB_PATH = "scan_results.db"

def analyze_fuzz_results():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()

    # Nađi payload-e koji su najčešće uspešni
    c.execute("SELECT payload, COUNT(*) as count FROM fuzz_results WHERE status_code >= 500 GROUP BY payload ORDER BY count DESC LIMIT 5")
    high_impact_payloads = c.fetchall()

    # Nađi ciljeve koji najčešće vraćaju 500/403 (indikatori slabosti)
    c.execute("SELECT target, COUNT(*) as count FROM fuzz_results WHERE status_code IN (403, 500) GROUP BY target ORDER BY count DESC LIMIT 5")
    vulnerable_targets = c.fetchall()

    # Nađi najduže odgovore (potencijalna refleksija, leak)
    c.execute("SELECT target, payload, MAX(content_length) FROM fuzz_results")
    longest_response = c.fetchone()

    conn.close()

    return {
        "high_impact_payloads": high_impact_payloads,
        "vulnerable_targets": vulnerable_targets,
        "longest_response": longest_response
    }

def print_analysis(report):
    print("\n[🧠 TAKTIČAR AI ANALIZA]")
    print("Top payload-i (status 500+):")
    for payload, count in report["high_impact_payloads"]:
        print(f"  - {payload} (x{count})")

    print("\nNajosetljivije mete (403/500):")
    for target, count in report["vulnerable_targets"]:
        print(f"  - {target} (x{count})")

    print("\nNajveći odgovor:")
    print(f"  - Target: {report['longest_response'][0]}")
    print(f"  - Payload: {report['longest_response'][1]}")
    print(f"  - Length: {report['longest_response'][2]} bytes")

if __name__ == "__main__":
    report = analyze_fuzz_results()
    print_analysis(report)
