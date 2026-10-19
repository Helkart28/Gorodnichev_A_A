max_streak = 0
current_streak = 1
prev = int(input("Введите первое число: "))
if prev != 0:
    max_streak = 1
    current = int(input("Введите следующее число: "))
    
    while current != 0:
        if current == prev:
            current_streak += 1
        else:
            if current_streak > max_streak:
                max_streak = current_streak
            current_streak = 1  # Сброс счетчика текущей серии
        prev = current
        current = int(input("Введите следующее число: "))
    if current_streak > max_streak:
        max_streak = current_streak
print("Наибольшее число подряд идущих равных элементов:", max_streak)