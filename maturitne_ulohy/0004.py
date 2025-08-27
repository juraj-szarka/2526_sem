f = open("content/meteo_data.txt", "r")

data_txt = f.read()


def data_handling(data_txt):
    data_list = data_txt.split("\n")
    data_sorted = []
    for each in data_list:
        each_splitted = each.split(" ")
        instance = {"station": each_splitted[0], "date": each_splitted[1], "time": each_splitted[2],
                    "temp": float(each_splitted[3].replace(",", ".").replace("--", "-").replace("+-", "")),
                    "cloudiness": each_splitted[4]}
        data_sorted.append(instance)
    return data_sorted

'''

    B O D Y

'''

def pocet_merani(data_given):
    return len(data_given)

def namerane_teploty(data_given):
    temps = []
    for each in data_given:
        temps.append(each["temp"])
    return temps

def najvyssia_teplota(data_given):
    temps = namerane_teploty(data_given)
    temps.sort()
    return temps[-1]

def kod_stanica_max(data_given):
    max = najvyssia_teplota(data_given)
    for each in data_given:
        if each["temp"] == max:
            return each["station"]

data = data_handling(data_txt)

print(pocet_merani(data))
print(namerane_teploty(data))
print(najvyssia_teplota(data))
print(kod_stanica_max(data))
