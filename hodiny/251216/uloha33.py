date = input('zadaj datum v tvare dd.mm.rrrr: ')

dni_v_mesiaci = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

day = int(date[0:2])
month = int(date[3:5])
year = int(date[6:10])

for i in range(month-1):
    day += dni_v_mesiaci[i]
    
if year % 4 == 0 and month > 2:
    day += 1
    
print(day)    
