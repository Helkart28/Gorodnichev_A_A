N = int(input())
first = 1
second = 1
summa = 0
for i in range(N):
    summa = summa + first
    new = first + second
    first = second
    second = new
print(summa)