import math

x = float(input("Введите переменную x: "))
y = float(input("Введите переменную y: "))
z = float(input("Введите переменную z: "))
s = math.exp(math.fabs(x - y)) * math.fabs(x - y) ** (x + y) / (math.atan(x) + math.atan(z)) + (x ** 6 + math.log(y) ** 2) ** (1 / 3)
print("s = {0:.4f}".format(s))