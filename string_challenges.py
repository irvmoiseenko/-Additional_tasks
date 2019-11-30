# Вывести последнюю букву в слове
word = 'Архангельск'
print(word[-1])


# Вывести количество букв "а" в слове
from collections import Counter
word = 'Архангельск'
count = Counter(word.lower())
print(count['а'])



# Вывести количество гласных букв в слове
word = 'Архангельск'
vowels = 0
for i in word:
    letter = i.lower()
    if letter == "а" or letter == "у" or letter == "о" or letter == "ы" or letter == "и" or letter == "э" or letter == "я" or letter == "ю" or letter == "ё" or letter == "е":
        vowels += 1
print(vowels)


# Вывести количество слов в предложении
sentence = 'Мы приехали в гости'
print(len(sentence.split())) 


# Вывести первую букву каждого слова на отдельной строке
sentence = 'Мы приехали в гости'
for word in sentence.split():
    print(word[0])


# Вывести усреднённую длину слова.
sentence = 'Мы приехали в гости'
a = sentence.split()
summ = 0
for word in a:
    srword = len(word) / len(a)
    summ += srword
print(summ)