import re

# відкриття файлу для читання та запису
with open('ct1_3_book_natalia.txt', 'r', encoding='utf-8') as input_file:
    # зчитування вмісту файлу
    text = input_file.read()

    # видалення не англійських символів з тексту
    english_text = re.sub('[^a-zA-Z\n]+', ' ', text)
    text_without_spaces = english_text.replace(" ", "")
    text_without_spaces = text_without_spaces.replace("\n", "")



# відкриття файлу для запису результату
with open('output2_crypted.txt', 'w', encoding='utf-8') as output_file:
    # запис результату в файл
    output_file.write(text_without_spaces)



