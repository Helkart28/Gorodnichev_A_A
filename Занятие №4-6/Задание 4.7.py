n = int(input())
factorial = 1 
summa = 0
for i in range(1, n + 1):
    factorial = factorial * i  
    summa = summa + factorial
print(summa)