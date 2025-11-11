import random

totalweight = 0
count = {}


while totalweight < 100 and len(count) < 15:
    name = input("Zadaj názov predmetu: ")
    if name.lower() == "vypis":
        for item, w in count.items():
            print(f"{item}: {w} kg")
    elif name in count:
        weight = int(input("Zadaj váhu predmetu (v kg): "))
        count[name] += weight
        totalweight += weight
    else:
        weight = int(input("Zadaj váhu predmetu (v kg): "))
        count[name] = weight
        totalweight += weight

for item, w in count.items():
    print(f"{item}: {w} kg")