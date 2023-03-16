import sys

def encrypt_vigenere_ukr(plaintext, keyword):
    #Шифрує відкритий текст методом шифрування Віженера
    ciphertext = ""
    keyword = keyword.upper()
    plaintext = plaintext.upper()
    i = 0
    for char in plaintext:
        if char.isalpha():
            shift = ord(keyword[i % len(keyword)]) - ord('А')
            ciphertext += chr((ord(char) - ord('А') + shift) % 33 + ord('А'))
            i += 1
            #якщо потрібно реаліхуватии без пропустків та інших знаків, то просто забрати елс
        else:
            ciphertext += char
    return ciphertext



plaintext = "Я люблю яблука."
key = "мило"


if len(plaintext) >= len(key):
    ciphertext = encrypt_vigenere_ukr(plaintext, key)
else:
    print("wrong key")
    sys.exit()
print(ciphertext) # "К УИПЧЕ ЙПЧЫХО"