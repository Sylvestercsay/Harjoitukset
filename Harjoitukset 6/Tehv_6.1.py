import random

def dice():
    return random.randint(1,6)

roll = 0

while roll != 6:
    roll = dice()
    print(roll)
