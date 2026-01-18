vuosi = int(input("Vuosi: "))

if vuosi % 4 != 0:
    print("Ei karkausvuosi")
elif vuosi % 100 != 0:
    print("Karkausvuosi")
elif vuosi % 400 == 0:
    print("Karkausvuosi")
else:
    print("Ei karkausvuosi")
