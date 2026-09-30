import math

x = float(input("Введите переменную x: "))
y = float(input("Введите переменную y: "))
z = float(input("Введите переменную z: "))
s = (x ** (y + 1) + math.exp(y - 1)) / (1 + x * math.fabs(y - math.tan(z))) * (1 + math.fabs(y - x)) + math.fabs(y - x) ** 2 / 2 - math.fabs(y - x) ** 3 / 3
print("s = {0:.7f}".format(s))