import random

numero = random.randint(1, 10)
laskea = 0

while laskea != numero:
    laskea = int(input("arvaa luku välillä :"))

    if laskea > numero:
        print("Liian suuri arvaus")

    elif laskea < numero:
        print("Liian pieni arvaus")

print("oikein")

