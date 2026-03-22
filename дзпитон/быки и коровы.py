# Чтение входных данных
secret, guess = map(int, input().split())

# Извлекаем цифры загаданного числа (A)
# Цифры: тысячи, сотни, десятки, единицы
secret_thousands = secret // 1000
secret_hundreds = (secret // 100) % 10
secret_tens = (secret // 10) % 10
secret_units = secret % 10

# Извлекаем цифры предложенного числа (B)
guess_thousands = guess // 1000
guess_hundreds = (guess // 100) % 10
guess_tens = (guess // 10) % 10
guess_units = guess % 10

# Подсчет быков (совпадение по значению и позиции)
bulls = 0

if secret_thousands == guess_thousands:
    bulls += 1
if secret_hundreds == guess_hundreds:
    bulls += 1
if secret_tens == guess_tens:
    bulls += 1
if secret_units == guess_units:
    bulls += 1

# Подсчет коров (цифры есть в обоих числах, но на разных позициях)
cows = 0

# Проверяем каждую цифру загаданного числа
# Цифра тысяч
if secret_thousands == guess_hundreds or secret_thousands == guess_tens or secret_thousands == guess_units:
    if secret_thousands != guess_thousands:  # Не считаем, если это уже бык
        cows += 1

# Цифра сотен
if secret_hundreds == guess_thousands or secret_hundreds == guess_tens or secret_hundreds == guess_units:
    if secret_hundreds != guess_hundreds:
        cows += 1

# Цифра десятков
if secret_tens == guess_thousands or secret_tens == guess_hundreds or secret_tens == guess_units:
    if secret_tens != guess_tens:
        cows += 1

# Цифра единиц
if secret_units == guess_thousands or secret_units == guess_hundreds or secret_units == guess_tens:
    if secret_units != guess_units:
        cows += 1

# Вывод результата
print(bulls, cows)