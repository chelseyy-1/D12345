# Чтение входных данных
A, B, C, D = map(int, input().split())

# Строка для хранения найденных корней
roots = ""

# Перебираем все возможные корни от -100 до 100
for x in range(-100, 101):
    # Вычисляем значение многочлена
    value = A * x ** 3 + B * x ** 2 + C * x + D
    
    # Если x является корнем
    if value == 0:
        # Проверяем, не встречался ли уже такой корень
        is_duplicate = False
        
        # Временная строка для обхода
        temp = roots
        # Переменная для накопления текущего корня из строки
        current_root = ""
        
        # Проходим по всей строке temp посимвольно
        for ch in temp:
            if ch == ' ':
                # Проверяем накопленный корень
                if current_root:
                    if int(current_root) == x:
                        is_duplicate = True
                        break
                    # Сбрасываем current_root для следующего числа
                    current_root = ""
            else:
                # Если не пробел, добавляем символ к текущему корню
                current_root += ch
        
        # После цикла проверяем последний корень
        if not is_duplicate and current_root:
            if int(current_root) == x:
                is_duplicate = True
        
        # Если корень новый, добавляем его
        if not is_duplicate:
            if roots:
                roots += " "
            roots += str(x)

# Вывод результата
print(roots)