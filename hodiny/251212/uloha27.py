# ----------------------------
# PONUKA KÁV - ZÁKLADNÉ CENY
# ----------------------------

napoje = [
    "Espresso",      # 0
    "Americano",     # 1
    "Latte",         # 2
    "Cappuccino",   # 3
    "Macchiato",    # 4
    "Mocha",        # 5
    "Flat White"    # 6
]

ceny_napojov = [2.50, 3.00, 2.50, 3.00, 2.50, 3.50, 2.50]

# ----------------------------
# VÝPIS PONUKY
# ----------------------------

print("PONUKA KÁV:")
# DOPLŇ príkazy na výpis ponuky nápojov aj s kódom nápoja,
# ktorý používateľ zadáva pri pvýbere nápoja- forma výpisu je na tebe.
for i in range(7):
    print(napoje[i], ceny_napojov[i])


# ----------------------------
# VSTUPY OD POUŽÍVATEĽA
# ----------------------------

volba = int(input("Zadaj číslo nápoja (0 - 6): "))
while volba < 0 or volba > 6:
    print("Neplatná voľba nápoja!")
    volba = int(input("Zadaj číslo nápoja (0 - 6): "))

velkost = input("Zadaj veľkosť (M, L, XL): ").upper()
while velkost not in ["M", "L", "XL"]:
    print("Neplatná veľkosť!")
    velkost = input("Zadaj veľkosť (M, L, XL): ").upper()

typ = input("Zadaj typ (IN / OUT): ").upper()
while typ not in ["IN", "OUT"]:
    print("Neplatný typ podania!")
    typ = input("Zadaj typ (IN / OUT): ").upper()

# ----------------------------
# PRÍPLATOK ZA VEĽKOSŤ
# ----------------------------

priplatok_velkost = [0, 1, 1.5]
# DOPLŇ príkazy na výpočet poplatku za veľkosť kávy
price = ceny_napojov[volba]
if velkost == "M":
    price += priplatok_velkost[0]
elif velkost == "L":
    price += priplatok_velkost[1]
elif velkost == "XL":
    price += priplatok_velkost[2]

# ----------------------------
# PRÍPLATOK ZA TYP PODANIA
# ----------------------------

if typ == "IN":
    price += 0
elif typ == "OUT":
    price += 1
    
# ----------------------------
# VÝPOČET CELKOVEJ CENY
# ----------------------------

cena_spolu = price  # DOPLŇ ako sa počíta celková cena kávy

# ----------------------------
# VÝPIS VÝSLEDKU
# ----------------------------

print()   
print("ZHRNUTIE OBJEDNÁVKY:")
print(f"Nápoj: {napoje[volba]}")                       # DOPLŇ názov nápoja ktorý si zákazník vybral
print("Veľkosť:", velkost)
print("Typ:", typ)
print(f"Cena spolu: {price}€")              # DOPLŇ výpis celkovej ceny objednávky
