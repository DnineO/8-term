# По заданной текстовой строке, состоящей из символов указанного алфавита,
# возвращает строку, зашифрованную с помощью шифра Цезаря.

# TODO:формировать алфавит по другому
list = ['А', 'Б', 'В', 'Г', 'Д', 'Е', 'Ё', 'Ж', 'З', 'И', 'Й', 'К', 'Л', 'М', 'Н', 'О', 'П', 'Р', 'С', 'Т', 'У', 'Ф',
        'Х', 'Ц', 'Ч', 'Ш', 'Щ', 'Ъ', 'Ы', 'Ь', 'Э', 'Ю', 'Я', '_']


# метод прохода заданной строки со сдвигом, return зашифрованную строку
def encrypt(text, count):
    result = ""

    for i in text:
        if i in list:
            param = list.index(i) % len(list)
            result += list[(param + count)]
        else:
            result += i
    return result


# По заданной строке, зашифрованной с помощью шифра Цезаря и состоящей из символов указанного алфавита, возвращает
# строку-оригинал.

# метод прохода по заданной строке со сдвигом, return оригинал

def decrypt(text, count):
    reslut = ""

    for i in text:
        if i in list:
            param = list.index(i)
            reslut += list[(param - count)]
        else:
            reslut += i

    return reslut


# метод атаки полным перебором

def full_bust(text):
    result = ""

    for z in range(len(list)):
        for i in text:
            if i in list:
                param = list.index(i)
                param -= z
                if param < 0:
                    param += len(list)
                result += list[param]
        print(z, result)
    return result


text1 = "РОМАН"
count = 7

print(text1, " сдвиг = ", count)
print("Зашифрованная: ", encrypt(text1, count))
text2 = encrypt(text1, count)
print("Расшифрованная: ", decrypt(text2, count))
print("Перебор", full_bust(text2))
