N = int(input())
K = int(input())
first = 1
second = 1
summa = 0
for i in range(1, K + N):
    if i >= K: 
        summa = summa + first
    new = first + second
    first = second
    second = new
print(summa)
