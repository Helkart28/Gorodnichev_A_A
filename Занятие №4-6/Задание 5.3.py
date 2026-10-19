N = int(input("Введите число N: "))
power = 0
current_value = 1
while current_value * 2 <= N:
    current_value *= 2
    power += 1
print("Показатель степени:", power)
print("Сама степень:", current_value)