from datetime import datetime

num = str(input('Zadaj rodné číslo: '))

year = ('20' if int(num[0:2]) < 26 else '19') + num[0:2]
month = num[2:4]
day = num[4:6]

yearn, monthn, dayn = datetime.now().year, datetime.now().month, datetime.now().day
print(year, month, day)

age = yearn - int(year) - 1
if int(month) < monthn:
    age += 1
elif int(month) == monthn and int(day) <= dayn:
    age += 1
    
gender = "žena" if int(month) > 20 else "muž"
if gender == "žena":
    month[0] = "0" if month[0] == 5 else "1"

print(f'{day}.{month}.{year}, {gender}, {age}')
