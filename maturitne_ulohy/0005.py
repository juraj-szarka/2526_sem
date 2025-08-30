f = open("content/objednane_jedla.txt", "r")

orders = f.read().split("\n")

def sum_orders(mylist):
    return len(mylist)

def sum_menu(mylist):
    sums = {"z": 0, "o": 0, "c": 0, "m": 0}
    for each in mylist:
        x = each.split(" ")
        sums[x[1]] += 1

    return sums

def twentyplus(mylist):
    sums = sum_menu(mylist)
    returnable = ""
    for each in sums:
        if sums[each] < 20:
            if returnable != "":
                returnable += f", {each}"
            else:
                returnable = f"nedostatok: {each}"
    if returnable == "":
        returnable = "dostatok"
    return returnable

print(sum_orders(orders))
print(sum_menu(orders))
print(twentyplus(orders))
