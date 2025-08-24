f = open("content/hada.txt", "r")

content = f.read()
line_list = content.split('\n')

def get_game_num(game_list = line_list):
    return len(game_list)

def get_longest_game(game_list = line_list):
    longest = ''
    for each in game_list:
        if len(each) > len(longest):
            longest = each
    return longest

def create_copy(game_list = line_list):
    result = ''
    comprimed = ''
    last = ''
    num = 0
    for each in game_list:
        for i in each:
            if num == 0:
                last = i
                num += 1
            elif i == last:
                num += 1
            else:
                comprimed = comprimed + last + str(num)
                last = i
                num = 1
        comprimed = comprimed + last + str(num)
        result += (comprimed + '\n')
        comprimed = ''
    with open("content/hada_copy_comprimed.txt", "w") as f2:
        f2.write(result)

    return result

print(get_game_num())
print(get_longest_game())
print(create_copy())