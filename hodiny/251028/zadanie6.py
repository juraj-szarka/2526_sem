with open("slovencina.txt", encoding='utf-8') as f:
    f_list = f.readlines()
letters_to_replace = f_list[0].strip()
text_lines = f_list[1:]

new_lines = []

for line in text_lines:
    new_line = line

    for letter in letters_to_replace:
        new_line = new_line.replace(letter, "_")
        new_line = new_line.replace(letter.upper(), "_")

    new_lines.append(new_line)

with open("slovencina_vystup.txt", "w", encoding='utf-8') as f:
    f.writelines(new_lines)

