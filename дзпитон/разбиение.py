# Чтение входных данных
N, M = map(int, input().split())

# Вычисляем базовое значение и остаток
base = N // M
remainder = N % M

# Строка для вывода результата
result = ""

# Выводим все числа в одном цикле
for i in range(M):
    if result:
        result += " "
    
    # Если остались большие числа, выводим base + 1
    if i >= M - remainder:
        result += str(base + 1)
    else:
        result += str(base)

print(result)