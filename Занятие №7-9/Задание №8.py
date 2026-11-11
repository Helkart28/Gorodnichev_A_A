#Задание 1
import math

def gipotenuza(a, b):
    return math.sqrt(a**2 + b**2)

print('Первый треугольник:')
a1 = float(input('Катет a: '))
b1 = float(input('Катет b: '))
print('Второй треугольник:')
a2 = float(input('Катет a: '))
b2 = float(input('Катет b: '))

c1 = gipotenuza(a1, b1)
c2 = gipotenuza(a2, b2)

print('Гипотенуза 1-го треугольника: {:.2f}'.format(c1))
print('Гипотенуза 2-го треугольника: {:.2f}'.format(c2))

if c1 > c2:
    print('Гипотенуза первого треугольника больше, второго - меньше')
elif c1 < c2:
    print('Гипотенуза второго треугольника больше, первого - меньше')
else:
    print('Гипотенузы равны')

    #Задание 2
    
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