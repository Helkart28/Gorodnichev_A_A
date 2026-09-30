def same_color(c1, r1, c2, r2):
    if (c1 + r1) % 2 == (c2 + r2) % 2:
        print("Да")
    else:
        print("Нет")
c1 = int(input())
r1 = int(input())
c2 = int(input())
r2 = int(input())
 
same_color(c1, r1, c2, r2)