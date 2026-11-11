def sort_word(word):
    letters = list(word)
    letters.sort()
    return ''.join(letters)

stroka = input('Введите строку: ')
words = stroka.split()

result = []
for w in words:
    result.append(sort_word(w))

print('Результат:', ' '.join(result))