import os
import sys

def clear():
    os.system('clear' if os.name == 'posix' else 'cls')

def show_menu():
    clear()
    print("╔════════════════════════════════════╗")
    print("║   SHADOWFOX14 – Command Center    ║")
    print("╠════════════════════════════════════╣")
    print("║ 1. 🎯 Upravljanje Metama           ║")
    print("║ 2. 🕵️ Recon – Priprema cilja       ║")
    print("║ 3. ⚔️ Napadi – Izbor i izvršenje    ║")
    print("║ 4. 🧬 Mutacije i AI analiza         ║")
    print("║ 5. 📜 Izveštaji i Validacija        ║")
    print("║ 6. 🧠 AI Savetnik i Rezime          ║")
    print("║ 7. 🧹 Reset i Čišćenje baze         ║")
    print("║ 8. 🚪 Izlaz                        ║")
    print("╚════════════════════════════════════╝")

def stub(name):
    print(f"\n[+] Pokrećem modul: {name}")
    print("   (Stub placeholder – modul se razvija...)\n")
    input("Pritisni ENTER za povratak u meni...")

def main():
    while True:
        show_menu()
        m = input("Izbor: ")
        if m == "1":
                    url = input("Unesi URL mete: ")
                    meta_control.add_target(url)
                    input("ENTER...")
        elif m == "2":
            from logic.option_02_recon_scan import run
            run()
        elif choice == "3":
            stub("Napadi – Izbor i izvršenje")
        elif choice == "4":
            stub("Mutacije i AI analiza")
        elif choice == "5":
            stub("Izveštaji i Validacija")
        elif choice == "6":
            stub("AI Savetnik i Rezime")
        elif choice == "7":
            stub("Reset i Čišćenje baze")
        elif choice == "8":
            print("\n[✓] Izlazim iz ShadowFox14...")
            break
        else:
            print("[!] Nevažeća opcija. Pokušaj ponovo.")
            input("Pritisni ENTER...")

if __name__ == "__main__":
    main()
