import random
elements = "+-*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
code_length = int(input('Длина пароля:'))
password = ''
for i in range(code_length):
    password += random.choice(elements)
print(password)
