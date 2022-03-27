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
    while count <=15:
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
        result += "000000000" + str(item)
    # print(result)
    return result


def encrypt(list, text):
    bytes = getBin32(list, text)
    print("32 bytes: ", bytes)
    result = ""
    for num in table31:
        result += bytes[num]
    encrypted = result
    print("Encrypted: ", encrypted)
    result = ""
    for i in range(len(encrypted)):
        # result +=
        i += 3 #TODO: 30 str


def bin2str(text):
    for i in range(len(text)):
        result = text[:len(text)-(len(text)-(i+8))] #TODO: 58 str


def main():
    # print("32 bytes: ", getBin32(byteList, message))
    randTable()
    encrypt(byteList, message)
    print("List: ", byteList)
    print("Rand numbers: ", table31)
    print(len(list2))
    print(len(table31))
    print(len(list1))
    print(len(table15))

main()

