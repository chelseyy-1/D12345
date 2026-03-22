# Чтение входных данных
time_str = input().strip()

# Извлекаем часы и минуты
hours = int(time_str[0:2])
minutes = int(time_str[3:5])

# Преобразуем время в минуты от начала суток
current_minutes = hours * 60 + minutes

# Функция проверки, является ли время палиндромом
# На входе часы и минуты
def is_palindrome(h, m):
    # Формируем строку времени
    # Часы всегда двузначные
    if h < 10:
        hour_str = "0" + str(h)
    else:
        hour_str = str(h)
    
    # Минуты всегда двузначные
    if m < 10:
        minute_str = "0" + str(m)
    else:
        minute_str = str(m)
    
    # Проверяем, является ли время палиндромом
    # HH:MM палиндром, если HH читается как перевернутое MM
    # Например, 12:21: hour_str="12", minute_str="21", reversed(minute_str)="12"
    
    # Получаем перевернутые минуты
    reversed_minutes = minute_str[1] + minute_str[0]
    
    return hour_str == reversed_minutes

# Ищем ближайшее палиндромное время
found = False
minutes_to_check = current_minutes

# Проверяем от текущего времени до конца суток
while minutes_to_check <= 24 * 60 - 1:
    h = minutes_to_check // 60
    m = minutes_to_check % 60
    
    if is_palindrome(h, m):
        found = True
        break
    minutes_to_check += 1

# Если не нашли до конца суток, проверяем с начала суток
if not found:
    minutes_to_check = 0
    while minutes_to_check < current_minutes:
        h = minutes_to_check // 60
        m = minutes_to_check % 60
        
        if is_palindrome(h, m):
            found = True
            break
        minutes_to_check += 1

# Вывод результата
if h < 10:
    print("0" + str(h) + ":", end="")
else:
    print(str(h) + ":", end="")

if m < 10:
    print("0" + str(m))
else:
    print(str(m))