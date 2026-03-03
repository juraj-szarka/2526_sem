nums = '01000001 01001000 01001111 01001010'

nums_splitted = nums.split(' ')
nums_resolved = []
text = ''
for i in nums_splitted:
    num = 0
    for j in range(8):
        print(j, i, int(i[-j-1], ))
        if int(i[-j-1]) != 0:
            num += (int(i[-j-1]) * 2) ** j
        print(num)
    print(num)
    text += chr(num)
    print(text)
    
print(text)