# Чтение дат
petya_date = input().strip()
vasya_date = input().strip()

# Извлекаем компоненты
petya_day = int(petya_date[0:2])
petya_month = int(petya_date[3:5])
petya_year = int(petya_date[6:8])

vasya_day = int(vasya_date[0:2])
vasya_month = int(vasya_date[3:5])
vasya_year = int(vasya_date[6:8])

# Приводим года к полному формату
petya_year = 1900 + petya_year
vasya_year = 1900 + vasya_year

# Количество дней в месяцах
days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

# Функция для вычисления количества дней от начала года
def days_from_start(month, day):
    total = 0
    i = 0
    while i < month - 1:
        total += days_in_month[i]
        i += 1
    total += day
    return total

# Дни от начала года
petya_start = days_from_start(petya_month, petya_day)
vasya_start = days_from_start(vasya_month, vasya_day)

# Подсчет разницы
difference = 0

# Если года разные
if petya_year < vasya_year:
    # Дни в году Пети после его дня рождения
    difference += 365 - petya_start
    
    # Полные годы между
    year = petya_year + 1
    while year < vasya_year:
        difference += 365
        year += 1
    
    # Дни в году Васи до его дня рождения
    difference += vasya_start
else:
    # Один год
    difference = vasya_start - petya_start

print(difference)