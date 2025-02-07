import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def tool_1():
    print("\n🔧 Tool 1 sélectionné !")
    input("Appuie sur Entrée pour revenir au menu...")

def tool_2():
    print("\n🔧 Tool 2 sélectionné !")
    input("Appuie sur Entrée pour revenir au menu...")

# Ajoute ici d'autres tools jusqu'à 10
tools = {
    "1": tool_1,
    "2": tool_2,
    # "3": tool_3,
    # "4": tool_4,
    # ...
}

def main():
    while True:
        clear_screen()
        print("="*40)
        print("🔥 MULTI TOOL MENU 🔥".center(40))
        print("="*40)
        print("\nSélectionne un outil :\n")
        
        for num in tools:
            print(f"[+] {num} : Tool {num}")

        print("\n[0] Quitter")
        
        choice = input("\n➜ Choix : ").strip()

        if choice == "0":
            print("\n👋 Bye !")
            break
        elif choice in tools:
            clear_screen()
            tools[choice]()
        else:
            print("\n⛔ Choix invalide !")
            input("Appuie sur Entrée pour réessayer...")

if __name__ == "__main__":
    main()
