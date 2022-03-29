import random

# initial data
list1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
list2 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29,
         30, 31]
message = "VL"
byteList = []
table31 = []
table15 = []
tableP = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29,
          30, 31]


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
        list.append(str(bin(ord(text[c])))[2:].rjust(16, '0'))


def getBin32(list, text):
    toBin(list, text)
    result = ""
    for item in list:
        result += str(item)
    return result


def PBlock(text):
    result = ""
    for num in table31:
        result += text[num]
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


def decPBlock(text):
    result = ""
    num = 0
    for num in tableP:
        for i in range(len(table31)):
            if table31[i] == num:
                index = i
                result += text[index]
    return result


def decSBlock(convert):
    decrypted = ""
    num = 0
    while num < len(convert):
        result = ""
        result += convert[num:num + 4]
        decrypted += decrypt4byte(result)
        num += 4
    return decrypted


def encrypt4byte(text):
    decimal = int(text, 2)
    encrypted_decimal = str(bin(list1[decimal]))[2:]
    return encrypted_decimal.rjust(4, "0")


def decrypt4byte(text):
    """ На вход поступают 4 бита """
    decimal = int(text, 2)
    for num in range(len(list1)):
        if decimal == list1[num]:
            result = str(bin(num))[2:].rjust(4, '0')
            return result


def getStrFromBin(string):
    result = ""
    num = 0
    while num < len(string):
        result += chr(int(string[num:num + 8], 2))
        num += 8
    return result


def encrypt(list, text):
    print("_______________________")
    bytes = getBin32(list, text)
    print("32 bytes: ", bytes)

    # Pblock
    pblock = PBlock(bytes)
    print("PBlock 1: ", pblock)

    # Sblock
    sblock = SBlock(pblock)
    print("SBlock:   ", sblock)
    # print(decSBlock(convert))

    # Pblock
    result = PBlock(sblock)
    print("PBlock 2: ", result)

    mess = getStrFromBin(result)
    print("message: ", mess)
    return result


def decrypt(text):
    print("_______________________")
    decrypted = decPBlock(text)
    print("Dec PBlock 2: ", decrypted)

    decS = decSBlock(decrypted)
    print("Dec SBlock: ", decS)

    res = decPBlock(decS)
    print("Dec PBlock 1: ", res)

    mess = getStrFromBin(res)
    print("message: ", mess)
    print("_______________________")
    return res


def main():
    print("_______________________")
    print("Enter message to encode (two symbols): ")
    message = input()

    print("Message: ", message)
    randTable()

    a = encrypt(byteList, message)
    decrypt(a)

    # print("List: ", byteList)
    # print("Rand numbers: ", table15)
    # print(table31)


main()
