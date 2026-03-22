# Чтение входных данных
number = input().strip()

# Длина числа
n = len(number)

# Преобразуем строку в список цифр для удобного доступа
# Но чтобы не использовать список, будем обращаться к строке напрямую

# Переменная для хранения максимальной суммы
max_sum = None

# Перебираем все позиции для удаления
for remove_pos in range(n):
    # Вычисляем плюс-минус сумму с пропуском позиции remove_pos
    current_sum = 0
    sign = 1  # 1 для плюса, -1 для минуса
    
    # Идем по всем цифрам исходного числа
    for i in range(n):
        if i == remove_pos:
            continue  # Пропускаем удаляемую цифру
        digit = int(number[i])
        current_sum += sign * digit
        sign = -sign  # Меняем знак для следующей цифры
    
    # Обновляем максимум
    if max_sum is None or current_sum > max_sum:
        max_sum = current_sum

# Выводим результат
print(max_sum)