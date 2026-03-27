with open('zamestnanci1.txt', 'r', encoding='UTF-8') as file:
    n = file.readlines()
    print(n)

l = 0
for i in n:
    i_s = i.strip().split()
    if int(i_s[2]) >= 30 and int(i_s[3]) >= 5:
        print(i_s[0], i_s[1])
        l += 1
        
print(l)