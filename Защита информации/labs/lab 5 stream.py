import random

# initial data
key = []
gen = []
gamma = []

def generate_key():
    for i in range(256):
        key.append(i)
    random.shuffle(key)
    for i in range(256):
        gen.append(key[i])
    # print(key, gen)


def generation_random_numbers():
    j = 0
    for i in range(256):
        j = (j + gen[i] + key[i]) % 256
        gen[j], gen[i] = gen[i], gen[j]
    return gen


def gamma(message, gen):
    i, j = 0, 0
    for k in range(len(message)):
        i = (i + 1) % 256


def main():
    print("запуск")
    generate_key()  # creating key and shuffle

    # print("1", key)
    # print("2", gen)

    # generation_random_numbers()
    # print(gen)


main()
