with open('medzery.txt' ,'r') as f:
    subor = f.readlines()

medzery = 0
for i in subor:
    for j in i:
        if j == ' ':
            medzery += 1
            
print(medzery)
