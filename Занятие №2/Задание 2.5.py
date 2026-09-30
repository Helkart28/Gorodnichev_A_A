import math

x = float(input("Введите переменную x: "))
y = float(input("Введите переменную y: "))
z = float(input("Введите переменную z: "))
s = math.log(y ** (-math.sqrt(math.fabs(x)))) * (x - y / 2) + math.sin(math.atan(z)) ** 2
print("s = {0:.3f}".format(s))