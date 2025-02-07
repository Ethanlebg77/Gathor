import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    while True:
        clear_screen()
        print("=" * 40)
        print("🔥 MULTI TOOL MENU 🔥".center(40))
        print("=" * 40)
        print("\nSélectionne un outil :\n")
        print("[1] Lookup Numéro de Téléphone")
        print("[2] Lookup IP")
        print("[3] Lookup Adresse Postale")
        print("\n[0] Quitter")

        choice = input("\n➜ Choix : ").strip()

        if choice == "1":
            os.system("Tools/PhoneLookup.py")
        elif choice == "2":
            os.system("Tools/IpLookup.py")
        elif choice == "3":
            os.system("Tools/AddressLookup.py")
        elif choice == "0":
            print("\n👋 Bye !")
            break
        else:
            print("\n⛔ Choix invalide !")
            input("Appuie sur Entrée pour réessayer...")

if __name__ == "__main__":
    main()
