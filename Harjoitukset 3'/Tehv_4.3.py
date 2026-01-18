numbers = []

käyttäjä = input("Syötä numero : ")

while käyttäjä != "":
    numbers.append(float(käyttäjä))
    käyttäjä = input("Syötä numero : ")

if numbers:
    print ("pieni määrä", min(numbers))
    print("Suurin lukumäärä", max(numbers))

else:
    print("Numero ei ole syötetty")


