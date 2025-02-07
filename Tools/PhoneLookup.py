
import requests

def phone_lookup():
    api_key = "TA_CLE_API"  # Remplace par une vraie clé API
    phone_number = input("📞 Entrez le numéro de téléphone : ")

    url = f"http://apilayer.net/api/validate?access_key={api_key}&number={phone_number}"

    try:
        response = requests.get(url).json()
        if response.get("valid"):
            print(f"\n📌 Pays : {response['country_name']}")
            print(f"📡 Opérateur : {response['carrier']}")
            print(f"📍 Région : {response['location']}")
        else:
            print("\n⛔ Numéro invalide !")
    except Exception as e:
        print("\n⚠ Erreur :", e)

    input("\nAppuie sur Entrée pour revenir au menu...")

if __name__ == "__main__":
    phone_lookup()
