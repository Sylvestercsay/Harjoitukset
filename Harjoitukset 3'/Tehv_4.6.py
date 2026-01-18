import random

pisteet = int(input("Syötä pisteet: "))

sisäpiiri= 0
laskea = 0

while laskea < pisteet:
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)

    if x * x + y * y < 1:
        sisäpiiri += 1

    laskea += 1

pi_approx = 4 * sisäpiiri / pisteet
print("Piin likiarvo:", pi_approx)
