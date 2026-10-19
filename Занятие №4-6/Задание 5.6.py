total_sum = 0
count = 0
num = int(input("Введите число последовательности: "))
while num != 0:
    total_sum += num
    count += 1
    num = int(input("Введите число последовательности: "))
if count > 0:
    average = total_sum / count
    print("Среднее значение:", average)
else:
    print("Последовательность пуста")