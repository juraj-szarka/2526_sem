with open('bmi.txt', 'r') as f:
    lines = f.readlines()
    
for line in lines:
    l = line[:-2].split(' ')
    bmi = float(l[0]) / (float(l[1]) ** 2)
    if bmi < 18.5:
        print('podvaha, vaha:', round(bmi, 2))
    elif bmi < 25:
        print('normalna hmotnost, vaha:', round(bmi, 2))
    elif bmi < 30:
        print('nadvaha, vaha:', round(bmi, 2))
    else:
        print('obezny, vaha:', round(bmi, 2))