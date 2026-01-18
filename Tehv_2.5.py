Leiviska = int(input("Syötä leiviskät: "))
Naula = int(input("Syötä naulat : "))
Luoti = int(input("Syötä luodit : "))

grammat = (Leiviska * 20 * 32 + Naula * 32 + Luoti) * 13.3

kilot = int(grammat / 1000)
grammat = grammat - kilot * 1000

print("Massa nykymittojen mukaan:")
print(kilot, "kilogrammaa ja", round(grammat, 2), "grammaa.")