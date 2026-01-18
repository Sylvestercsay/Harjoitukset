cabin = input("Anna hyttiluokka (LUX, A, B, C): ")

if cabin == "LUX":
    print("Yläkannen parvekkeellinen hytti.")
elif cabin == "A":
    print("Hytti, jossa on ikkuna autokannen yläpuolella.")
elif cabin == "B":
    print("Ikkunaton hytti autokannen yläpuolella.")
elif cabin == "C":
    print("Ikkunaton hytti autokannen alapuolella.")
else:
    print("Virheellinen hyttiluokka.")

