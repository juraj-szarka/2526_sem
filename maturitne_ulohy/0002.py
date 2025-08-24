f = open("hada.txt", "r")

content = f.read()
line_list = content.split('\n')

print(f)
print('')
print(content)
print('')
print(line_list)

print('')

def get_game_num(game_list = line_list):
    return len(game_list)

print(get_game_num())