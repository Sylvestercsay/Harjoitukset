import random

class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = 0
        self.matka = 0




    def kiihdytä(self, nopeuden_muutos):
        self.nopeus += nopeuden_muutos
        if self.nopeus < 0:
            self.nopeus = 0
        if self.nopeus > self.huippunopeus:
            self.nopeus = self.huippunopeus

    def kulje(self, aika):
        self.matka += (self.nopeus * aika)


class Kilpailu:
    def __init__(self, nimi, kilometrit, autot):
         self.nimi = nimi
         self.kilometrit = kilometrit
         self.autot = autot

    def tunti_kuluu(self):
        for auto in self.autot:
            nopeuden_muutos = random.randint(-10,15)
            auto.kiihdytä(nopeuden_muutos)
            auto.kulje(1)

    def tulosta_tilanne(self):
        print("Rekisteri    Huippunopeus    Nopeus    Matka")
        print("----------------------------------------------")
        for auto in self.autot:
            print(auto.rekisteritunnus, "        ", auto.huippunopeus, "        ", auto.nopeus, "      ", auto.matka)

    def kilpailu_ohi(self):
        for auto in self.autot:
            if auto.matka >= self.kilometrit:
                return True
        return False


autot = []
for i in range(1, 11):
    auto = Auto("ABC-" + str(i), random.randint(100, 200))
    autot.append(auto)

kilpailu = Kilpailu("Suuri romuralli", 8000, autot)

print("Kilpailu alkaa:", kilpailu.nimi)
print("Matka:", kilpailu.kilometrit, "km")

tunnit = 0
while not kilpailu.kilpailu_ohi():
    kilpailu.tunti_kuluu()
    tunnit = tunnit + 1
    if tunnit % 10 == 0:
        print("\nTunti:", tunnit)
        kilpailu.tulosta_tilanne()

print("\nKilpailu päättyi", tunnit, "tunnin jälkeen!")
kilpailu.tulosta_tilanne()
