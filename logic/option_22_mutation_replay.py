# logic/option_22_mutation_replay.py
import sqlite3
from rich import print
from core.database import get_db_connection

def list_mutations():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id, original_id, mutated_payload, mutation_type, created_at FROM mutations ORDER BY created_at DESC LIMIT 10")
    rows = cursor.fetchall()
    conn.close()
    return rows

def replay_mutation(mutation_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT mutated_payload FROM mutations WHERE id = ?", (mutation_id,))
    result = cursor.fetchone()
    conn.close()
    if result:
        payload = result[0]
        print(f"[bold cyan]Replaying Mutation:[/bold cyan] {payload}")
        # Ovde bi išao replay sistem (stub za sada)
        print("[green]Replayed payload (simulacija)[/green]")
    else:
        print("[red]Nema mutacije sa tim ID-jem[/red]")

if __name__ == "__main__":
    mutations = list_mutations()
    if not mutations:
        print("[yellow]Nema mutacija u bazi[/yellow]")
    else:
        print("[bold blue]Poslednje mutacije:[/bold blue]")
        for row in mutations:
            print(f"[{row[0]}] ⮕ ID:{row[1]} | {row[2]} ({row[3]}) @ {row[4]}")
        try:
            choice = int(input("\nUnesi ID mutacije za replay: "))
            replay_mutation(choice)
        except ValueError:
            print("[red]Neispravan unos[/red]")
