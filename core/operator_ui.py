from rich.console import Console
from rich.table import Table
import sqlite3

def show_operator_dashboard():
    console = Console()
    conn = sqlite3.connect("shadowfox.db")
    cursor = conn.cursor()

    # Prikaz modula
    table = Table(title="🌐 SHADOWFOX OPERATOR: Detektovani Moduli")

    table.add_column("ID", style="cyan", no_wrap=True)
    table.add_column("Vreme", style="green")
    table.add_column("Modul", style="magenta")

    cursor.execute("SELECT id, timestamp, module FROM operator_log ORDER BY id DESC LIMIT 10")
    rows = cursor.fetchall()
    for row in rows:
        table.add_row(str(row[0]), row[1], row[2])

    console.print(table)

    # Prikaz grešaka
    error_table = Table(title="❗ Nedostajuće Tabele")

    error_table.add_column("ID", style="red", no_wrap=True)
    error_table.add_column("Vreme", style="yellow")
    error_table.add_column("Tabela", style="bold red")

    cursor.execute("SELECT id, timestamp, missing_table FROM operator_errors ORDER BY id DESC LIMIT 10")
    errors = cursor.fetchall()
    if errors:
        for err in errors:
            error_table.add_row(str(err[0]), err[1], err[2])
        console.print(error_table)
    else:
        console.print("[bold green]✅ Sve ključne tabele su prisutne![/bold green]")

    conn.close()

if __name__ == "__main__":
    show_operator_dashboard()
