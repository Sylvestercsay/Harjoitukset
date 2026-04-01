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

    def aja(self, tunnit):
        self.matka += self.nopeus * tunnit


class SahkoAuto(Auto):
    def __init__(self, rekisteritunnus, huippunopeus, akkukapasiteetti):
        super().__init__(rekisteritunnus, huippunopeus)
        self.akkukapasiteetti = akkukapasiteetti


class BensiiniAuto(Auto):
    def __init__(self, rekisteritunnus, huippunopeus, tankinkoko):
        super().__init__(rekisteritunnus, huippunopeus)
        self.tankinkoko = tankinkoko


sahko = SahkoAuto("ABC-15", 180, 52.5)
bensa = BensiiniAuto("ACD-123", 165, 32.3)

sahko.kiihdytä(100)
bensa.kiihdytä(120)

sahko.aja(3)
bensa.aja(3)

# Print kilometer counters
print(f"Sähkoäuto {sahko.rekisteritunnus} ajomatka: {sahko.matka} km")
print(f"Bensiiniauto {bensa.rekisteritunnus} ajomatka: {bensa.matka} km")
