count_greater = 0
prev = int(input("Введите первое число: "))
if prev != 0:
    current = int(input("Введите следующее число: "))
    while current != 0:
        if current > prev:
            count_greater += 1
        prev = current
        current = int(input("Введите следующее число: "))
print("Количество элементов больше предыдущего:", count_greater)