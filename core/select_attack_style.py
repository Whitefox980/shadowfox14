import sqlite3

def list_attack_styles():
    conn = sqlite3.connect("core/shadowfox.db")
    c = conn.cursor()

    c.execute("SELECT id, name, speed, mode, note FROM attack_styles")
    styles = c.fetchall()

    print("\n[📌] Dostupni stilovi napada:\n")
    for s in styles:
        print(f"({s[0]}) {s[1]} | Speed: {s[2]} | Mode: {s[3]} → {s[4]}")

    conn.close()
    return styles

def select_attack_style():
    styles = list_attack_styles()
    try:
        choice = int(input("\n[?] Izaberi stil (ID): "))
        selected = next((s for s in styles if s[0] == choice), None)
        if selected:
            print(f"\n[✓] Izabran stil: {selected[1]}")
            return selected[0]
        else:
            print("[!] Neispravan izbor.")
            return None
    except Exception as e:
        print(f"[!] Greška: {e}")
        return None

if __name__ == "__main__":
    select_attack_style()
