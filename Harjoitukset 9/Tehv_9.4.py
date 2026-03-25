import random

class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = 0
        self.matka = 0

    def tulosta_tiedot(self):
        print(f"{self.rekisteritunnus:<10} {self.huippunopeus:<15} {self.nopeus:<15} {self.matka:<15.1f}")

    def kiihdytä(self, nopeuden_muutos):
        self.nopeus += nopeuden_muutos
        if self.nopeus < 0:
            self.nopeus = 0
        if self.nopeus > self.huippunopeus:
            self.nopeus = self.huippunopeus

    def aja(self, tunnit):
        self.matka += self.nopeus * tunnit


autot = []
for i in range(1, 11):
    rekisteri = f"ABC-{i}"
    huippunopeus = random.randint(100, 200)
    autot.append(Auto(rekisteri, huippunopeus))


race_over = False
while not race_over:
    for auto in autot:
        auto.kiihdytä(random.randint(-10, 15))
        auto.aja(1)
        if auto.matka >= 10000:
            race_over = True

print(f"{'Rekisteri':<10} {'Huippunopeus':<15} {'Nopeus':<15} {'Matka (km)':<15}")
print("-" * 55)
for auto in autot:
    auto.tulosta_tiedot()
