A = int(input())
B = int(input())
if A < B:
    for i in range(A, B + 1):
        print(i, end=" ")
else:
    i = A
    while i >= B:
        print(i, end=" ")
        i = i - 1
print()