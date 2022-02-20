
small_symbols = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя_"
big_symbols = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ_"


def shift(text, symbols, n):
    index = symbols.find(text)
    if index + n < len(symbols):
        return symbols[index + n]
    else:
        return symbols[(index + n) % len(symbols)]


def back_shift(text, symbols, n):
    index = symbols.find(text)
    if index - n >= 0:
        return symbols[index - n]
    else:
        return symbols[(index - n) % len(symbols)]


def encrypt(text, n=3):
    res = ""

    for i in range(0, len(text)):
        if text[i].isupper():
            res += shift(text[i], big_symbols, n)

        elif text[i].islower():
            res += shift(text[i], small_symbols, n)
        else:
            res += text[i]

    return res


def decrypt(text, n=3):
    res = ""

    for i in range(0, len(text)):
        if text[i].isupper():
            res += back_shift(text[i], big_symbols, n)

        elif text[i].islower():
            res += back_shift(text[i], small_symbols, n)
        else:
            res += text[i]

    return res


str = encrypt(input())
print(str)
print(decrypt(str))
