room = None
finished = False

while room == None:
    try:
        room = int(input('Zadajte číslo izby: '))
    except:
        continue

def validation(room: int) -> list:
    if not 0 < room < 708:
        return "Neplatné číslo izby!"
    else:
        return f"Izba {room} je na poschodí {(room - 1)//7}"

print(validation(room))
