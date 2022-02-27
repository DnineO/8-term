# код для реализации Hill Cipher
keyMatrix = [[0] * 3 for i in range(3)]

# Создать вектор для сообщения
messageVector = [[0] for i in range(3)]

# Генерация вектора для шифра
cipherMatrix = [[0] for i in range(3)]


# Следующая функция генерирует
# ключевая матрица для ключевой строки
def getKeyMatrix(key):
    k = 0
    for i in range(3):
        for j in range(3):
            keyMatrix[i][j] = ord(key[k]) % 65
            k += 1


# Следующая функция шифрует сообщение
def encrypt(messageVector):
    for i in range(3):
        for j in range(1):
            cipherMatrix[i][j] = 0
            for x in range(3):
                cipherMatrix[i][j] += (keyMatrix[i][x] * messageVector[x][j])
            cipherMatrix[i][j] = cipherMatrix[i][j] % 26


def HillCipher(message, key):
    # Получить матрицу ключей из ключевой строки
    getKeyMatrix(key)

    # Создать вектор для сообщения
    for i in range(3):
        messageVector[i][0] = ord(message[i]) % 65

    # Следующая функция генерирует
    # зашифрованный вектор
    encrypt(messageVector)

    # Генерация зашифрованного текста
    # из зашифрованного вектора
    CipherText = []

    for i in range(3):
        CipherText.append(chr(cipherMatrix[i][0] + 65))

    # Наконец распечатать зашифрованный текст
    print("Ciphertext: ", "".join(CipherText))



def main():
    # Получить сообщение
    # быть зашифрованным
    message = "ACT"

    # Получить ключ
    key = "GYBNQKURP"

    HillCipher(message, key)


if __name__ == "__main__":
    main()