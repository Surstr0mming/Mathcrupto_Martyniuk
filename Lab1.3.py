import re

import matplotlib.pyplot as plt


with open('Cryptedtext.txt', 'r', encoding='utf-8') as input_file:
    # зчитування вмісту файлу
    cryptotext = input_file.read()
print(cryptotext, "\n")
cryptotext = re.sub('[^a-zA-Z\n]+', ' ', cryptotext)
print(cryptotext, "\n")
cryptotext = cryptotext.replace(" ", "")
print(cryptotext, "\n")
cryptotext = cryptotext.replace("\n", "")
print(cryptotext, "\n")
cryptotext = cryptotext.lower()
print(cryptotext)

key = "lemon"
alphabet = "abcdefghijklmnopqrstuvwxyz"

vigenere_table = []
for i in range(len(alphabet)):
    row = alphabet[i:] + alphabet[:i]
    vigenere_table.append(row)
key = key.lower()
key_index = 0
print_index = 0
ciphertext = ""
for char in cryptotext:
    char_index = alphabet.index(char.lower())
    key_char_index = alphabet.index(key[key_index])
    ciphertext += vigenere_table[key_char_index][char_index]
    key_index = (key_index + 1) % len(key)
    print_index += 1

cryptotext = ciphertext
IC_average = []
list_key = []
for i in range(5, 21):
    list_key.append(i)
    text = []
    for i_string in range(0, i):
        text_crypto = ""
        for i_text in range(len(cryptotext)):
            if i_text % i == i_string:
                text_crypto += cryptotext[i_text]
        text.append(text_crypto)
        full_IC = 0
    for itext in range(len(text)):
        #print(f"{itext + 1}.", text[itext])
        letter_count = {}

        # Проходимо по кожному символу у рядку
        for letter in text[itext]:
            # Якщо символ не є пробілом
            if letter.isalpha():
                # Додаємо символ до словника, якщо його там ще немає
                if letter not in letter_count:
                    letter_count[letter] = 1
                # Якщо символ вже є в словнику, збільшуємо його лічильник на 1
                else:
                    letter_count[letter] += 1

        # Виводимо кількість кожної букви
        IC = 0
        for letter in letter_count:
            IC = IC + letter_count[letter] * (letter_count[letter] - 1)
        IC = IC / (len(text[itext]) * (len(text[itext]) - 1))
        full_IC = full_IC + IC
    average = full_IC / i
    IC_average.append(average)



decrypt = {}
decrypt_keys = []
for i_key_average in range(len(IC_average)):
    if IC_average[i_key_average] > 0.058:
        decrypt[i_key_average + 5] = {IC_average[i_key_average]}
        decrypt_keys.append(i_key_average + 5)
print(decrypt)
print(decrypt_keys)
alhabet = {'a': .0855, 'b': .0155, 'c': .0316, 'd': .0387,
           'e': .126, 'f': .0218, 'g': .0209, 'h': .0496,
           'i': .0733, 'j': .0022, 'k': .0081, 'l': .0421,
           'm': .0253, 'n': .0717, 'o': .0747, 'p': .0207,
           'q': .001, 'r': .0633, 's': .0673, 't': .0894,
           'u': .0268, 'v': .0106, 'w': .0183, 'x': .0019,
           'y': .0172, 'z': .0011}
alhabet_full = 'abcdefghijklmnopqrstuvwxyz'

chi2_min = 999999999999
chi2_key = []
i_number = 1
number = 0

for i_decrypt in range(len(decrypt_keys)):
    chi2_nunberofstring = []
    i_number = 1
    for i_key_decrypt in range(decrypt_keys[i_decrypt]):
        decrypted_text = ""
        for i_full_text in range(len(cryptotext)):
            if i_full_text % decrypt_keys[i_decrypt] == i_key_decrypt:
                decrypted_text += cryptotext[i_full_text]
        #print(f"{i_number}.", decrypted_text)
        i_number += 1


        chi2_min = 9999999999999
        for i_slide in range(26):
            decrypted_text_new = ""
            for letter_slide in decrypted_text:
                if letter.isalpha():
                    decrypted_text_new += chr((ord(letter_slide) - 97 - 1) % 26 + 97)
            chi2 = 0
            letter_count_chi = {}
            for letter_chi in decrypted_text:
                # Якщо символ не є пробілом
                if letter_chi != " ":
                    # Додаємо символ до словника, якщо його там ще немає
                    if letter_chi not in letter_count_chi:
                        letter_count_chi[letter_chi] = 1
                    # Якщо символ вже є в словнику, збільшуємо його лічильник на 1
                    else:
                        letter_count_chi[letter_chi] += 1
            for letter_list in alhabet_full:
                if letter_list not in letter_count_chi:
                    letter_count_chi[letter_list] = 0
            for letter_chi in alhabet_full:
                chi2 += ((letter_count_chi[letter_chi] - len(decrypted_text_new) * alhabet[letter_chi]) *
                         (letter_count_chi[letter_chi] - len(decrypted_text_new) * alhabet[letter_chi])) / (
                                len(decrypted_text_new) * alhabet[letter_chi])
            if chi2 < chi2_min:
                chi2_min = chi2
                if i_slide == 25:
                    number = 0
                else:
                    number = i_slide + 1
            decrypted_text = decrypted_text_new
        chi2_nunberofstring.append(chr(97 + number - 1))
    print(f" for {decrypt_keys[i_decrypt]} :", chi2_nunberofstring)



key = ""
for i in range(decrypt_keys[0]):
    key += chi2_nunberofstring[i]
print(key)






#Дешифрує текст з використанням шифру Віженера з ключем
plaintext = ""
key_index = 0
for letter in cryptotext:
    if letter.isalpha():
        key_letter = key[key_index % len(key)]
        shift = ord(key_letter.upper()) - ord('A')
        if letter.isupper():
            plaintext += chr((ord(letter) - shift - 65) % 26 + 65)
        else:
            plaintext += chr((ord(letter) - shift - 97) % 26 + 97)
        key_index += 1
    else:
        plaintext += letter


print(plaintext)



with open('output2_decrypted.txt', 'w', encoding='utf-8') as output_file:
    # запис результату в файл
    output_file.write(plaintext)


y_plt = []
for i_plt in range(len(IC_average)):
    y_plt.append(i_plt + 5)
plt.bar(y_plt, IC_average)
plt.show()
