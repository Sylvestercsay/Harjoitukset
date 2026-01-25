import random

def noppa(kasvot):
    return random.randint(1, kasvot)

kasvot = int(input("Syötä kasvojen lukumäärä: "))

tulokset = 0

while tulokset != kasvot:
    tulokset = noppa(kasvot)
    print(tulokset)