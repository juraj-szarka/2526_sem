lines = []
with open('narodeniny.txt', 'r') as f:
    lines = f.readlines()
    

mesiac = input("zadajte mesiac ako cislo: ")
for i in range(0, len(lines), 3):
    date = lines[i+2]
    date_splitted = date.split()
    if date_splitted[1] == mesiac:
        print(lines[i], lines[i + 1], lines[i + 2])
