f = open("content/meteo_data.txt", "r")

data_txt = f.read()


def data_handling(data_txt):
    data_list = data_txt.split("\n")
    data_sorted = []
    for each in data_list:
        each_splitted = each.split(" ")
        instance = {"station": each_splitted[0], "date": each_splitted[1], "time": each_splitted[2],
                    "temp": each_splitted[3], "cloudiness": each_splitted[4]}
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
        temps.append(float(each["temp"].replace(",", ".").replace("--", "-").replace("+-", "")))
    return temps

def najvyssia_teplota(data_given):
    temps = namerane_teploty(data_given)
    temps.sort()
    return temps[-1]

data = data_handling(data_txt)

print(pocet_merani(data))
print(namerane_teploty(data))
print(najvyssia_teplota(data))
