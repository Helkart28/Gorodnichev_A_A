seconds = int(input("Введите количество секунд: "))

days = seconds // 86400           
hours = (seconds % 86400) // 3600 
minutes = (seconds % 3600) // 60 
sec = seconds % 60 

print(f"{days}:{hours}:{minutes}:{sec}")
