import random

# initial data
key = []
gen = []
gamma = []


# генерация ключа
def generate_key():
    for i in range(256):
        key.append(i)
    random.shuffle(key)
    for i in range(256):
        gen.append(key[i])
    # random.shuffle(gen) # можно и так, но есть generation_random_numbers
    # print(key, gen)


# генерация случайных чисел
def generation_random_numbers():
    j = 0
    for i in range(256):
        j = (j + gen[i] + key[i]) % 256
        gen[j], gen[i] = gen[i], gen[j]
    return gen


# получение гаммы
def create_gamma(message, gen):
    temp = gen
    # print(temp)

    i, j = 0, 0
    for k in range(len(message)):
        i = (i + 1) % 256
        j = (j + temp[i]) % 256
        temp[i], temp[j] = temp[j], temp[i]
        t = (temp[i] + temp[j]) % 256
        gamma.append(temp[t])
    return gamma


# получение списка кодов сообщения разбитых на 2 части
def str2bin(message):
    list = []
    for i in range(len(message)):
        list.append(bin(ord(message[i]))[2:].zfill(16)[:8])
        list.append(bin(ord(message[i]))[2:].zfill(16)[8:])
    # print(list)

    result = []

    for elem in list:
        num = 0
        str = elem[::-1]  # переворачиваем elem
        # print(str)
        for i in range(len(str)):
            num += int(str[i]) * (2 ** i)
        result.append(num)
    return result


# перевод в символы
def bin2str(message):
    symbols = ""
    num = 0
    while num < len(message):
        bit1 = bin(message[num])[2:].zfill(8)
        bit2 = bin(message[num+1])[2:].zfill(8)

        number = bit1 + bit2
        number = number[::-1]
        bit = 0
        for i in range(len(number)):
           bit += int(number[i]) * (2 ** i)

        symbols += chr(bit)
        num += 2
    return symbols


# шифрование сообщения
def encrypt(message, gamm):
    bytes = []
    for i in range(len(message)):
        bytes.append(message[i] ^ gamm[i])
    return bytes


# расшифровка сообщения
def decrypt(message, gamm):
    bytes = []
    for i in range(len(message)):
        bytes.append(message[i] ^ gamm[i])
    return bytes


# main function
def main():
    print("launch")
    generate_key()  # получение начального ключа

    # print ключа и gen, одинаковых
    print("Key: ", key[:10])
    # print("Generated random numbers", gen)

    generation_random_numbers()  # генерация случайных чисел
    print("Gen: ", gen[:10])

    print("Enter message: ")  # задание сообщения
    message = input()
    print("Message: ", [ord(letter) for letter in message])  # коды символов

    split = str2bin(message)  # получение пар байт сообщения
    print("Split message: ", split)

    create_gamma(split, gen)  # получение гаммы
    print("Gamma: ", gamma)

    enc = encrypt(split, gamma)  # шифруем сообщение
    print("Encrypted: ", enc)

    symbols = bin2str(enc)  # в символьном виде
    print("Symbols: ", symbols)

    unsplit = str2bin(symbols)  # получаем пары байт
    print("Split symbols: ", unsplit)

    decr = decrypt(unsplit, gamma)
    print("Decrypted: ", decr)

    end = bin2str(decr)
    print("Final message: ", end)

# TODO: можно объединить функции в одну шифровку и рассшифровку


main()
