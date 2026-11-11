#Задание 1
n = int(input('Введите длину массива: '))
D = []
for i in range(n):
    print('Введите', i, 'элемент:')
    D.append(int(input()))

s = 0
for i in range(1, n, 2):  
    s += D[i]

print('Массив D:', D)
print('Сумма элементов с нечётными индексами:', s)

#Задание 2
a = []
for i in range(8):
    print('Введите', i, 'элемент:')
    a.append(int(input()))

for i in range(8):
    if a[i] < 15:
        a[i] = a[i] * 2

print('Преобразованный массив:', a)
 
