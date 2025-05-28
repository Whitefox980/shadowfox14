import os
from pathlib import Path

DATA_FILE = Path("data/targets.txt")

def ensure_data_file():
    DATA_FILE.parent.mkdir(parents=True, exist_ok=True)
    if not DATA_FILE.exists():
        DATA_FILE.write_text("")

def add_target(url):
    ensure_data_file()
    with open(DATA_FILE, "a") as f:
        f.write(f"{url.strip()}\n")
    print(f"[+] Dodata meta: {url}")

def load_targets():
    ensure_data_file()
    with open(DATA_FILE, "r") as f:
        return [line.strip() for line in f.readlines() if line.strip()]

def clear_targets():
    ensure_data_file()
    DATA_FILE.write_text("")
    print("[✓] Svi ciljevi obrisani.")

def get_random_target():
    import random
    targets = load_targets()
    if targets:
        return random.choice(targets)
    return None
