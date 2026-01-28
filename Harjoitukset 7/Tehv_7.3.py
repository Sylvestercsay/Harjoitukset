lentoasemat = {}

while True:
    print("\nValitse toiminto:")
    print("1 - Syötä uusi lentoasema")
    print("2 - Hae lentoaseman tiedot")
    print("0 - Lopeta")

    valinta = input("Valintasi: ")

    if valinta == "1":
        icao = input("Syötä lentoaseman ICAO-koodi: ").upper()
        nimi = input("Syötä lentoaseman nimi: ")
        lentoasemat[icao] = nimi
        print(f"Lentoasema {nimi} tallennettu.")

    elif valinta == "2":
        haku = input("Syötä haettavan lentoaseman ICAO-koodi: ").upper()
        if haku in lentoasemat:
            print(f"Lentoaseman nimi on: {lentoasemat[haku]}")
        else:
            print("ICAO-koodia ei löytynyt.")

    elif valinta == "0":
        print("Heippa!")
        break

    else:
        print("Virheellinen valinta, yritä uudelleen.")