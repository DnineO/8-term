import random

# initial data
list1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
list2 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29,
         30, 31]
message = "ab"
byteList = []
table31 = []
table15 = []



def randTable():
    random.shuffle(list2)
    random.shuffle(list1)

    count = 0
    while count <= 31:
        table31.append(list2[count])
        count += 1

    count = 0
    while count <= 15:
        table15.append(list1[count])
        count += 1


def toBin(list, text):
    for c in range(len(text)):
        # print(str(bin(ord(message[c])))[2:])
        list.append(str(bin(ord(text[c])))[2:])


def getBin32(list, text):
    toBin(list, text)
    result = ""
    for item in list:
        result += str(item) + "000000000"
    # print(result)
    return result


def PBlock(bytes):
    result = ""
    for num in table31:
        result += bytes[num]
    return result


def SBlock(bytes):
    convert = ""
    num = 0
    while num < len(bytes):
        result = ""
        result += bytes[num:num + 4]
        convert += encrypt4byte(result)
        num += 4
    return convert


def decSBlock(convert):
    decrypted = ""
    num = 0
    while num < len(convert):
        result = ""
        result += convert[num:num + 4]
        decrypted += decrypt4byte(result)
        num += 4

    # print(decrypted)
    return decrypted


# noinspection PyStatementEffect
def encrypt4byte(text):
    decimal = int(text, 2)

    encrypted_decimal = str(bin(list1[decimal]))[2:]
    # print(result)
    return encrypted_decimal.ljust(4, "0")


def decrypt4byte(text):
    """ На вход поступают 4 бита """
    decimal = int(text, 2)

    for num in range(len(list1)):
        if decimal == list1[num]:
            #TODO: проверить
            result = str(bin(num))[2:].ljust(4, '0')
    # result = index
            return result


def encrypt(list, text):
    bytes = getBin32(list, text)
    print("32 bytes: ", bytes)

    # Pblock
    # encrypted = PBlock(bytes)
    # print("PBlock: ", encrypted)

    # Sblock
    convert = SBlock(bytes)
    print("SBlock: ", convert)
    print(decSBlock(convert))

    # Pblock
    # result = PBlock(convert)
    # print("PBlock: ", result)


def decrypt(list, text):
    convert = ""
    num = 0
    # print(len(encrypted))
    while num < len(encrypted):
        result = ""
        result += decrypted[num:num + 4]
        convert += decrypt4byte(result)
        num += 4
    # result -> convert
    print("SBlock: ", convert)

def main():
    #     # print("32 bytes: ", getBin32(byteList, message))


    print("Message: ", message)
    randTable()
    #     # print(encrypt4byte("1100"))
    #     print(decrypt4byte())

    a = encrypt(byteList, message)


    print("List: ", byteList)
    print("Rand numbers: ", table31)


#     # print(len(list2))
#     # print(len(table31))
#     # print(len(list1))
#     # print(len(table15))

main()
