total = 0
items = []

while len(items) < 15 and total <= 100:
    new_item = input('enter your product name or type "VYPIS" for item list: ')
    if new_item == 'VYPIS':
        print(items)
        continue
    new_item_weight = int(input('enter your product weight (in kg, without decimals): '))
    total += new_item_weight
    items.append(new_item)

print('KONIEC')
        