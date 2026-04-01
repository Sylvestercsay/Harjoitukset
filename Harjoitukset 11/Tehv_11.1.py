class Julkaisu:
    def __init__(self, nimi):
        self.nimi = nimi

class Kirja(Julkaisu):
    def __init__(self, nimi, tekija, sivumaara):
        super().__init__(nimi)
        self.tekija = tekija
        self.sivumaara = sivumaara

    def tulosta_tiedot(self):
        print(f"Nimi: {self.nimi}")
        print(f"Kirjoittaja: {self.tekija}")
        print(f"Sivut: {self.sivumaara}")

class Aikakauslehti(Julkaisu):
    def __init__(self, nimi, paatoimittaja):
        super().__init__(nimi)
        self.paatoimittaja = paatoimittaja

    def tulosta_tiedot(self):
        print(f"Nimi: {self.nimi}")
        print(f"Päätoimittaja: {self.paatoimittaja}")


lehti = Aikakauslehti("Donald Duck", "Aki Hyyppä")
kirja = Kirja("Compartment No. 6", "Rosa Liksom", 192)

lehti.tulosta_tiedot()

kirja.tulosta_tiedot()