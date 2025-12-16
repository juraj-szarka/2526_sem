with open(r'C:\Users\jsz\Desktop\teploty.txt', 'r') as f:
    lines = f.readlines()
    
temps_sum = 0
temps_i = len(lines)
for line in lines:
    temp = line.strip()
    temp = temp.replace(',', '.')
    temps_sum += float(temp)
    
print('priemerna teplota v juny bola:', temps_sum / temps_i)
