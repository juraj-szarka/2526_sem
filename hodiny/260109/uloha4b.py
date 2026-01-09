with open('zamestnanci.txt', 'r') as f:
    lines = f.readlines()
    
n = 0
for line in lines:
    p = line.split()
    if int(p[-1]) >= 5 and int(p[-2]) >= 30:
        print(p[0])
        n += 1

print('Pocet zamestnancov: ', n)
