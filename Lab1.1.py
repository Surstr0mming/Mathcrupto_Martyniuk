import re
import matplotlib.pyplot as plt

# Відкрити файл і зчитати вміст
with open('file.txt', 'r') as file:
    text = file.read()
text = text.lower()
text = text.replace(" ", "")
text = text.replace("\n", "")
text = re.sub('[^абвгґдеєжзиіїйклмнопрстуфхцчшщьюя\n]+', ' ', text)



letter_count = {}
alphabet = "абвгґдеєжзиіїйклмнопрстуфхцчшщьюя"

# Проходимо по кожному символу у рядку
for letter in text:
    # Якщо символ не є пробілом
    if letter.isalpha():
        # Додаємо символ до словника, якщо його там ще немає
        if letter not in letter_count:
            letter_count[letter] = 1
        # Якщо символ вже є в словнику, збільшуємо його лічильник на 1
        else:
            letter_count[letter] += 1
for letter_list in alphabet:
    if letter_list not in letter_count:
        letter_count[letter_list] = 0
print(len(letter_count))
print(letter_count)
for i in range(len(letter_count)):
    print(alphabet[i], letter_count[alphabet[i]])
letters = []
statics = []
for i in range(len(letter_count)):
    letters.append(alphabet[i])
    statics.append(letter_count[alphabet[i]]/len(text))

print(letters)
print(statics)

plt.bar(letters, statics)
plt.show()