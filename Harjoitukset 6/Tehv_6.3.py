def muunna_litroiksi(gallons):
    return gallons * 3.785

while True:
    g = float(input("Syötä gallonaa (negatiivinen arvo lopettaa): "))
    if g < 0:
        break
    print("Litraa:", muunna_litroiksi(g))