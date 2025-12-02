with open('stretnutie.txt', 'r') as file:
    bytes_list = file.readlines()
    
result = ''

for byte in bytes_list:
    result += chr(int(byte, 2))
    
print(result)
