import math

x = float(input("Введите переменную x: "))
y = float(input("Введите переменную y: "))
z = float(input("Введите переменную z: "))
s = (1 + math.sin(x + y) ** 2) / math.fabs(x - 2 * y / (1 + x ** 2 * y ** 2)) * x ** math.fabs(y) + math.cos(math.atan(1 / z)) ** 2
print("s = {0:.5f}".format(s))