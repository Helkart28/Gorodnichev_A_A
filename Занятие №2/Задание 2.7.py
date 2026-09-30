import math

x = float(input("Введите переменную x: "))
y = float(input("Введите переменную y: "))
z = float(input("Введите переменную z: "))
s = 5 * math.atan(x) - 1 / 4 * math.acos(x) \
    * (x + 3 * math.fabs(x - y) + x ** 2) / (math.fabs(x - y) * z + x ** 2)
print("s = {0:.3f}".format(s))