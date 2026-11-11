#Задание 1
n = int(input('Введите порядок матрицы: '))
A = []
for i in range(n):
    B = []
    for j in range(n):
        print('Введите [', i, ',', j, '] элемент')
        B.append(int(input()))
    A.append(B)

print('Матрица:')
for i in range(n):
    for j in range(n):
        print(A[i][j], end=' ')
    print()

symmetric = True
for i in range(n):
    for j in range(i + 1, n):
        if A[i][j] != A[j][i]:
            symmetric = False

if symmetric:
    print('Матрица симметрична')
else:
    print('Матрица не симметрична')

#Задание 2
n = int(input('Введите количество строк: '))
m = int(input('Введите количество столбцов: '))
A = []
for i in range(n):
    B = []
    for j in range(m):
        print('Введите [', i, ',', j, '] элемент')
        B.append(float(input()))
    A.append(B)

print('Исходная матрица:')
for i in range(n):
    for j in range(m):
        print(A[i][j], end=' ')
    print()

# поиск максимального элемента и его позиции
max_i = 0
max_j = 0
for i in range(n):
    for j in range(m):
        if A[i][j] > A[max_i][max_j]:
            max_i = i
            max_j = j

# перестановка строк: максимальная строка становится первой
tmp = A[0]
A[0] = A[max_i]
A[max_i] = tmp

# перестановка столбцов: максимальный столбец становится первым
for i in range(n):
    tmp = A[i][0]
    A[i][0] = A[i][max_j]
    A[i][max_j] = tmp

print('Полученная матрица:')
for i in range(n):
    for j in range(m):
        print(A[i][j], end=' ')
    print()
