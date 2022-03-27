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
f = open('lab2permutations.txt', 'w')
numberSwap = 1


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

def encrypt(num,perm):
    if (num <0 or num > perm-1):
            print("error")


def decrypt():
    print("decrypt")

def print2file(_str):
    number = 1
    while nxtSet(_str, n):
        f.write(str(str(number) + ' '))
        if number == 565:
            print()
        # print(number, printPere(alphabet, n))
        printPere(_str, n)
        f.write(' \n')
        number += 1
    return number #возвращает число перестановок


numberSwap = print2file(alphabet)


# АИНУТ_
f.close()

# АУА_ТН_АНИННТТТ
# ТУТ_АННА_И_НАТА

# Т_Н_ИИНИУИАИАУ_
# ТУТ_АННА_И_НАТА
