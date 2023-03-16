
import collections
import matplotlib.pyplot as plt

# Відкрити файл і зчитати вміст
with open('output2_crypted.txt', 'r') as file:
    text = file.read()

# Підрахувати кількість входжень кожної літери. Абсолютно всі символи з тексту
counter = collections.Counter(text.lower())

# Відфільтрувати  тільки літери
counter = {letter: count for letter, count in counter.items() if letter.isalpha()}

# Побудувати гістограму
plt.bar(counter.keys(), counter.values())
plt.show()
