user_time = int(input("Введите время в секундах : "))
seconds = user_time % 60
minutes = (user_time // 60) % 60
hours = user_time // 3600
print(hours, ':', minutes, ':', seconds)