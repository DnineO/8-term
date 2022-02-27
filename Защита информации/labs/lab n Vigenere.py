import array

# Алфавит
alphabet = ['А', 'И', 'Н', 'Т', 'У', '_']
# CONSTANT
n = len(alphabet)
# Ключ
key = 'АИ_'
# Сообщение
origstr = 'ТУТ_АННА_И_НАТА'


# def dictionary():
#     dict = {}
#     count = 0
#     for i in range(0, n):
#         dict[count] = chr(i)
#         count += 1
#     return dict
#
# def encode_str2number(str):
#     list = []
#     lenstr = len(str)
#     dict = dictionary()
#
#     for i in range(lenstr):
#         for value in dict:
#             # print(i, value)
#             if str[i] == dict[value]:
#                 list.append(value)
#     return list





def num2str(i):
    arr = ('А', 'И', 'Н', 'Т', 'У', '_')
    i = i % len(arr)
    # print(arr[i])
    return arr[i]


def str2num(ch):
    ch = ch.upper()
    arr = {'А': 0, 'И': 1, 'Н': 2, 'Т': 3, 'У': 4, '_': 5}
    # print(arr[ch])
    return arr[ch]


# C = (S + K) mod N, где S - номер символа в строке, K - номер символа в столбце
def encode(str, keyl):
    result = ''
    for (i, j) in enumerate(str):
        i = i % len(keyl)
        result += num2str(str2num(j) + str2num(keyl[i]))
        # print(result)
    return result


# C = (S + K + N) mod N, расшифровка
def decode(str, keyl):
    result = ''
    for (i, j) in enumerate(str):
        i = i % len(keyl)
        result += num2str(str2num(j) - str2num(keyl[i]))
        # print(result)
    return result


print(encode(origstr, key))
enstr = encode(origstr, key)
print(decode(enstr, key))

# print(dictionary(), alphabet)
# print(encode_str2number(origstr), encode_str2number(key))

# АУА_ТН_АНИННТТТ
# ТУТ_АННА_И_НАТА

# Т_Н_ИИНИУИАИАУ_
# ТУТ_АННА_И_НАТА
