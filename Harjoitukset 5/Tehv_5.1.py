import random

noppa = int(input("Syötä noppien numero :" ))

summa = 0

for i in range(noppa):
    roll = random.randint(1,6)
    summa += roll

print("Noppien summa on:", summa)