def menu():
    print("\nMINIBIUDŽETAS")
    print("1. Įvesti pajamas")
    print("2. Įvesti išlaidas")
    print("3. Atspausdinti pajamų eilutes")
    print("4. Atspausdinti išlaidų eilutes")
    print("5. Atspausdinti statistiką")
    print("q. Išeiti")


def ivesti_pajamas(pajamos):
    data = input("Įveskite datą (YYYY-MM-DD): ")
    pavadinimas = input("Įveskite pajamų pavadinimą: ")
    suma = float(input("Įveskite sumą: "))
    pajamos.append([data, pavadinimas, suma])


def ivesti_islaidas(islaidos):
    data = input("Įveskite datą (YYYY-MM-DD): ")
    pavadinimas = input("Įveskite išlaidų pavadinimą: ")
    suma = float(input("Įveskite sumą: "))
    islaidos.append([data, pavadinimas, suma])


def spausdinti_eilutes(eilutes, pavadinimas):
    print(f"\n{pavadinimas.upper()}:")
    for i, eilute in enumerate(eilutes):
        print(f"{i}: {eilute[0]}, {eilute[1]}, {eilute[2]:.2f} EUR")


def spausdinti_statistika(pajamos, islaidos):
    pajamos_suma = sum(item[2] for item in pajamos)
    islaidos_suma = sum(item[2] for item in islaidos)
    balansas = pajamos_suma - islaidos_suma
    print("\nSTATISTIKA:")
    print(f"Bendra pajamų suma: {pajamos_suma:.2f} EUR")
    print(f"Bendra išlaidų suma: {islaidos_suma:.2f} EUR")
    print(f"Balansas: {balansas:.2f} EUR")