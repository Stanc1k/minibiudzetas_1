def menu():
    print("\nMINIBIUDŽETAS")
    print("1. Įvesti pajamas")
    print("2. Įvesti išlaidas")
    print("3. Atspausdinti pajamų eilutes")
    print("4. Atspausdinti išlaidų eilutes")
    print("5. Atspausdinti statistiką")
    print("q. Išeiti")


import funkcijos
import pickle

# Pagrindiniai sąrašai
try:
    with open("data.pkl", "rb") as f:
        data = pickle.load(f)
        pajamos = data.get("pajamos", [])
        islaidos = data.get("islaidos", [])
except FileNotFoundError:
    pajamos = []
    islaidos = []

while True:
    funkcijos.menu()
    choice = input("Pasirinkite veiksmą: ")
    if choice == "1":
        funkcijos.ivesti_pajamas(pajamos)
    elif choice == "2":
        funkcijos.ivesti_islaidas(islaidos)
    elif choice == "3":
        funkcijos.spausdinti_eilutes(pajamos, "Pajamos")
    elif choice == "4":
        funkcijos.spausdinti_eilutes(islaidos, "Išlaidos")
    elif choice == "5":
        funkcijos.spausdinti_statistika(pajamos, islaidos)
    elif choice.lower() == "q":
        with open("data.pkl", "wb") as f:
            pickle.dump({"pajamos": pajamos, "islaidos": islaidos}, f)
        print("Programa baigta.")
        break
    else:
        print("Neteisingas pasirinkimas.")
