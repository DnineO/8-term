import numpy as np
from egcd import egcd  # pip install egcd

# alphabet = "abcdefghijklmnopqrstuvwxyz"
alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"

letter_to_index = dict(zip(alphabet, range(len(alphabet))))
index_to_letter = dict(zip(range(len(alphabet)), alphabet))


def matrix_mod_inv(matrix, modulus):
    """We find the matrix modulus inverse by
    Step 1) Find determinant
    Step 2) Find determinant value in a specific modulus (usually length of alphabet)
    Step 3) Take that det_inv times the det*inverted matrix (this will then be the adjoint) in mod N
    """

    det = int(np.round(np.linalg.det(matrix)))  # Step 1)
    det_inv = egcd(det, modulus)[1] % modulus  # Step 2)
    matrix_modulus_inv = (
            det_inv * np.round(det * np.linalg.inv(matrix)).astype(int) % modulus
    )  # Step 3)

    return matrix_modulus_inv


def encrypt(message, K):
    encrypted = ""
    message_in_numbers = []

    for letter in message:
        message_in_numbers.append(letter_to_index[letter])

    split_P = [
        message_in_numbers[i: i + int(K.shape[0])]
        for i in range(0, len(message_in_numbers), int(K.shape[0]))
    ]

    for p in split_P:
        p = np.transpose(np.asarray(p))[:, np.newaxis]

        while p.shape[0] != K.shape[0]:
            p = np.append(p, letter_to_index[" "])[:, np.newaxis]

        numbers = np.dot(K, p) % len(alphabet)
        n = numbers.shape[0]  # length of encrypted message (in numbers)

        # Map back to get encrypted text
        for idx in range(n):
            number = int(numbers[idx, 0])
            encrypted += index_to_letter[number]

    return encrypted


def decrypt(cipher, Kinv):
    decrypted = ""
    cipher_in_numbers = []

    for letter in cipher:
        cipher_in_numbers.append(letter_to_index[letter])

    split_C = [
        cipher_in_numbers[i: i + int(Kinv.shape[0])]
        for i in range(0, len(cipher_in_numbers), int(Kinv.shape[0]))
    ]

    for c in split_C:
        c = np.transpose(np.asarray(c))[:, np.newaxis]
        numbers = np.dot(Kinv, c) % len(alphabet)
        n = numbers.shape[0]

        for idx in range(n):
            number = int(numbers[idx, 0])
            decrypted += index_to_letter[number]

    return decrypted


def main():
    # message = 'my life is potato'
    # message = "helpmeplease"
    message = "азбука"

    # K = np.matrix([[3, 20], [2, 16]])
    # K = np.matrix([[6, 2, 10], [13, 16, 10], [20, 17, 15]])
    K = np.matrix([[3, 10, 20], [20, 19, 17], [23, 78, 17]])
    Kinv = matrix_mod_inv(K, len(alphabet))

    encrypted_message = encrypt(message, K)
    decrypted_message = decrypt(encrypted_message, Kinv)

    print("Original message: " + message)
    print("Encrypted message: " + encrypted_message)
    print("Decrypted message: " + decrypted_message)


main()
