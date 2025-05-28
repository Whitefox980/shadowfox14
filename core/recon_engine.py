import os
import subprocess
import json
from datetime import datetime

RECON_DIR = "data/recon_data"

def create_output_file(meta_url, tool_name):
    hostname = meta_url.replace("https://", "").replace("http://", "").split("/")[0]
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    os.makedirs(RECON_DIR, exist_ok=True)
    return f"{RECON_DIR}/{hostname}_{tool_name}_{timestamp}.json", hostname

def run_subfinder(meta_url):
    output_file, host = create_output_file(meta_url, "subfinder")
    cmd = f"subfinder -d {host} -silent -o {output_file.replace('.json', '.txt')}"
    subprocess.run(cmd, shell=True)
    with open(output_file.replace('.json', '.txt'), 'r') as f:
        lines = [x.strip() for x in f if x.strip()]
    with open(output_file, 'w') as out:
        json.dump({"subdomains": lines}, out, indent=2)
    return output_file

def run_gau(meta_url):
    output_file, host = create_output_file(meta_url, "gau")
    cmd = f"gau {host} > {output_file.replace('.json', '.txt')}"
    subprocess.run(cmd, shell=True)
    with open(output_file.replace('.json', '.txt'), 'r') as f:
        endpoints = [x.strip() for x in f if x.strip()]
    with open(output_file, 'w') as out:
        json.dump({"endpoints": endpoints}, out, indent=2)
    return output_file

def run_httpx(meta_url):
    output_file, host = create_output_file(meta_url, "httpx")
    cmd = f"echo {meta_url} | httpx -title -status-code -tech-detect -json -o {output_file}"
    subprocess.run(cmd, shell=True)
    return output_file

def run_hakrawler(meta_url):
    output_file, host = create_output_file(meta_url, "hakrawler")
    cmd = f"echo {meta_url} | hakrawler -depth 2 -plain > {output_file.replace('.json', '.txt')}"
    subprocess.run(cmd, shell=True)
    with open(output_file.replace('.json', '.txt'), 'r') as f:
        endpoints = [x.strip() for x in f if x.strip()]
    with open(output_file, 'w') as out:
        json.dump({"endpoints": endpoints}, out, indent=2)
    return output_file

def run_nuclei(meta_url):
    output_file, host = create_output_file(meta_url, "nuclei")
    cmd = f"echo {meta_url} | nuclei -silent -json -o {output_file}"
    subprocess.run(cmd, shell=True)
    return output_file

def full_recon(meta_url):
    print(f"[RECON] Počinjem duboku analizu za: {meta_url}")
    results = {
        "subfinder": run_subfinder(meta_url),
        "gau": run_gau(meta_url),
        "httpx": run_httpx(meta_url),
        "hakrawler": run_hakrawler(meta_url),
        "nuclei": run_nuclei(meta_url)
    }
    print(f"[RECON] Završena. Fajlovi: {results}")
    return results
