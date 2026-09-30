def count_equal(z, x, c):
    if z == x and x == c:
        print(3)
    elif z == x or z == c or x == c:
        print(2)
    else:
        print(0)
z = int(input())
x = int(input())
c = int(input()) 
 
count_equal(z, x, c)
 