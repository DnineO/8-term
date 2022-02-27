import array

# Алфавит
alphabet = ['А', 'И', 'Н', 'Т', 'У', '_']
# CONSTANT
n = len(alphabet)
# Ключ
key = 'АИ_'
# Сообщение
origstr = 'ТУТ_АННА_И_НАТА'
# file
f = open('lab2result.txt', 'w')


# def file():

def swap(a, i, j):
    s = a[i]
    a[i] = a[j]
    a[j] = s


def nxtSet(a, n):
    j = n - 2
    while j != -1 and a[j] >= a[j + 1]:
        j -= 1
    if j == -1:
        return False

    k = n - 1
    while (a[j] >= a[k]):
        k -= 1
    swap(a, j, k)

    l = j + 1
    r = n - 1
    while (l < r):
        swap(a, l, r)
        l += 1
        r -= 1
    return True


def printPere(a, n):
    pere = ''
    for i in range(n):
        pere += str(a[i])
    f.write(pere)
    # print(pere)
    # f.write('\n')
    return pere


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


# printPere(alphabet,n)
number = 1
while nxtSet(alphabet, n):
    f.write(str(str(number) + ' '))
    if number == 565:
        print()
    # print(number, printPere(alphabet, n))
    printPere(alphabet, n)
    f.write(' \n')
    number += 1

# АИНУТ_

f.close()

# print(encode(origstr, key))
# enstr = encode(origstr, key)
# print(decode(enstr, key))

# АУА_ТН_АНИННТТТ
# ТУТ_АННА_И_НАТА

# Т_Н_ИИНИУИАИАУ_
# ТУТ_АННА_И_НАТА
