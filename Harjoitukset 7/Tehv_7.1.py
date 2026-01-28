vuodenajat = ("", "talvi", "talvi", "kevät", "kevät", "kevät", "kesä", "kesä", "kesä", "syksy", "syksy", "syksy", "talvi")


kuukausi = int(input("Anna kuukauden numero (1-12): "))

if 1 <= kuukausi <= 12:
    print(f"{kuukausi}. kuukausi kuuluu vuodenaikaan: {vuodenajat[kuukausi]}")
else:
    print("Virhe: Anna luku väliltä 1-12.")