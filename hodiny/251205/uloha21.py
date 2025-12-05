import random

eggs = int(input("zadaj pocet vajec: "))
big = eggs // 12
small = (eggs - 12 * big) // 6
rest = eggs - big*12 - small*6

print(f"""
treba {big} velkych skatul,
{small} malych skatul, 
na ranajky budes mat {rest} vajec
""")
