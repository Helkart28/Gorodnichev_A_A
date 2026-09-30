import math

x = float(input("Введите переменную x: "))
y = float(input("Введите переменную y: "))
z = float(input("Введите переменную z: "))
s = math.sqrt(10 * (x ** (1 / 3) + x ** (y + 2))) * (math.asin(z) ** 2 - math.fabs(x - y))
print("s = {0:.4f}".format(s))