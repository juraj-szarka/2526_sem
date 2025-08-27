f = open("content/meteo_data.txt", "r")

data = f.read()

def pocet_merani(data_txt):
    data_splitted = data_txt.split("\n")
    return len(data_splitted)

print(pocet_merani(data))