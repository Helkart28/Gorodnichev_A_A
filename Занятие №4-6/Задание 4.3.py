A = int(input())
B = int(input())
i = A
while i >= B:
    if i % 2 != 0: 
        print(i, end=" ")
    i = i - 1
print()