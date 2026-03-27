amount = input('Zadaj sumu v tvare "3.19": ')
amount_dec = float(amount)
amount_cent = amount_dec * 100
amount_cent = int(amount_cent)

print('mas', amount_cent // 200, 'mimncu v hodnote 200 centov')
amount_cent %= 200
print('mas', amount_cent // 100, 'mimncu v hodnote 100 centov')
amount_cent %= 100
print('mas', amount_cent // 50, 'mimncu v hodnote 50 centov')
amount_cent %= 50
print('mas', amount_cent // 20, 'mimncu v hodnote 20 centov')
amount_cent %= 20
print('mas', amount_cent // 10, 'mimncu v hodnote 10 centov')
amount_cent %= 10
print('mas', amount_cent // 5, 'mimncu v hodnote 5 centov')
amount_cent %= 5
print('mas', amount_cent // 2, 'mimncu v hodnote 2 centov')
amount_cent %= 2
print('mas', amount_cent // 1, 'mimncu v hodnote 1 centov')
amount_cent %= 1

