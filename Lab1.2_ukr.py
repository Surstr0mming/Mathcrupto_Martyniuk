import sys


def generate_vigenere_table():
    #Генерує таблицю Віженера
    alphabet = "абвгґдеєжзиіїйклмнопрстуфхцчшщьюя"
    vigenere_table = []
    for i in range(len(alphabet)):
        row = alphabet[i:] + alphabet[:i]
        vigenere_table.append(row)
    return vigenere_table

def vigenere_encrypt(plaintext, key):
    #Шифрує відкритий текст методом шифрування Віженера
    alphabet = "абвгґдеєжзиіїйклмнопрстуфхцчшщьюя"
    vigenere_table = generate_vigenere_table()
    key = key.lower()
    key_index = 0
    print_index = 0
    ciphertext = ""

    for char in plaintext:
        if char.isalpha():
            char_index = alphabet.index(char.lower())
            key_char_index = alphabet.index(key[key_index])
            ciphertext += vigenere_table[key_char_index][char_index]
            key_index = (key_index + 1) % len(key)

            print("char = ", alphabet[char_index])
            print("char_index = ", char_index)

            print("key_char = ", alphabet[key_char_index])
            print("key_char_index = ", key_char_index)


            print("cipherletter = ", ciphertext[print_index])
            print("ciphertext = ", ciphertext)
            print("\n")
            print_index += 1

    return ciphertext


plaintext = "Я люблю їсти лимони"
key = "ключ"



if len(plaintext) >= len(key):
    ciphertext = vigenere_encrypt(plaintext, key)
else:
    print("wrong key")
    sys.exit()
print(ciphertext)
print("\n\n\n")

vigenere_table = generate_vigenere_table()
for i in range(len(vigenere_table)):
    print(vigenere_table[i])