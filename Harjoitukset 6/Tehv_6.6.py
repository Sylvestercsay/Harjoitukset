import math

def yksikköhinta(d, hinta):
    r = d / 2 / 100
    area = math.pi * r**2
    return hinta / area

d1 = float(input("Pizza 1 halkaisija (cm): "))
p1 = float(input("Pizza 1 hinta (€): "))
d2 = float(input("Pizza 2 halkaisija (cm): "))
p2 = float(input("Pizza 2 hinta (€): "))

up1 = yksikköhinta(d1, p1)
up2 = yksikköhinta(d2, p2)

print("Pizzan yksikköhinta 1: {:.2f} €/m²".format(up1))
print("Pizzan yksikköhinta  2: {:.2f} €/m²".format(up2))

if up1 < up2:
    print("Pizza 1 on hintansa arvoinen.")
elif up2 < up1:
    print("Pizza 2 on parempi vastine rahalle.")
else:
    print("Molemmat pizzat ovat samanarvoisia..")
