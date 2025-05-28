# logic/option_02_recon_scan.py

from core.recon_engine import full_recon
from data.targets_store import get_all_targets

def run():
    metas = get_all_targets()
    if not metas:
        print("[!] Nema meta u bazi. Prvo ih unesi kroz opciju 1.")
        return

    for meta_url in metas:
        print(f"[•] Pokrećem recon za: {meta_url}")
        rezultati = full_recon(meta_url)
        print("[✓] Završeno za:", meta_url)
        for alat, fajl in rezultati.items():
            print(f"   → {alat}: {fajl}")
