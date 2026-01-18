gender = input("mies vai nainen: ")
hb = int(input("Hemoglobiiniarvo (g/l): "))

if gender == "nainen":
    if hb < 117:
        print("Matala")
    elif hb <= 175:
        print("Normaali")
    else:
        print("Korkea")

if gender == "mies":
    if hb < 134:
        print("Matala")
    elif hb <= 195:
        print("Normaali")
    else:
        print("Korkea")
