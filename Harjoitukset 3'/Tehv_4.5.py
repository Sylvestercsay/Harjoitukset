oikea_käyttäjätunnus = "python"
oikea_salasana = "säänöt"

attempts = 0
while attempts < 5:
    käyttäjätunnus = input("käyttäjätunnus: ")
    salasana = input("salasana: ")

    if käyttäjätunnus == oikea_käyttäjätunnus and salasana == oikea_salasana:
        print("Tervetuloa")
        break
    else:
        attempts += 1

if attempts == 5:
    print("Pääsy evätty")