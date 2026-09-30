import math

x = float(input("Введите переменную x: "))
y = float(input("Введите переменную y: "))
z = float(input("Введите переменную z: "))
s = math.fabs(x ** (y / x) - (y / x) ** (1 / 3)) + (y - x) * (math.cos(y) - z / (y - x)) / (1 + (y - x) ** 2)
print("s = {0:.5f}".format(s))