price = float(input("Zadaj cenu v eurach (napr. '4.18'): "))

rounded_price = round(float(price), 2)
cents = int(round(rounded_price * 100))

if cents >= 200:
    print(f"mas {cents // 200}{'mince' if cents // 200 > 1 else 'mincu'} v hodnote {200} centov")
    cents = cents % 200
if cents >= 100:
    print(f"mas {cents // 100}{'mince' if cents // 100 > 1 else 'mincu'} v hodnote {100} centov")
    cents = cents % 100
if cents >= 50:
    print(f"mas {cents // 50}{'mince' if cents // 50 > 1 else 'mincu'} v hodnote {50} centov")
    cents = cents % 50
if cents >= 20:
    print(f"mas {cents // 20}{'mince' if cents // 20 > 1 else 'mincu'} v hodnote {20} centov")
    cents = cents % 20
if cents >= 10:
    print(f"mas {cents // 10}{'mince' if cents // 10 > 1 else 'mincu'} v hodnote {10} centov")
    cents = cents % 10
if cents >= 5:
    print(f"mas {cents // 5}{'mince' if cents // 5 > 1 else 'mincu'} v hodnote {5} centov")
    cents = cents % 5
if cents >= 2:
    print(f"mas {cents // 2}{'mince' if cents // 2 > 1 else 'mincu'} v hodnote {2} centov")
    cents = cents % 2
if cents >= 1:
    print(f"mas {cents // 1}{'mince' if cents // 1 > 1 else 'mincu'} v hodnote {1} centov")
    cents = cents % 1
