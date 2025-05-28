def load_targets_from_txt(path='data/targets.txt'):
    try:
        with open(path, 'r') as f:
            lines = [line.strip() for line in f if line.strip()]
        return list(set(lines))  # bez duplikata
    except FileNotFoundError:
        print(f"[!] Fajl '{path}' ne postoji.")
        return []
