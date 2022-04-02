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


def create_gamma(message, gen):
    temp = gen
    # print(temp)

    i, j = 0, 0
    for k in range(len(message)):
        i = (i + 1) % 256
        j = (j + temp[i]) % 256
        temp[i], temp[j] = temp[j], temp[i]
        t = (temp[i] + temp[j]) % 256
        gamma.append(temp[t])
    return gamma


def num2bin(num,pos):



def encrypt(text):
    gamm = create_gamma(text, gen)
    bytes = []


def main():
    print("запуск")
    generate_key()  # creating key and shuffle

    print("Enter message: ")
    message = input()

    # print("1", key)
    # print("2", gen)

    # generation_random_numbers()
    # print(gen)

    # print("",create_gamma(message, gen))



main()
