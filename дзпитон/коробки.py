# Чтение размеров первой коробки
A1, B1, C1 = map(int, input().split())

# Чтение размеров второй коробки
A2, B2, C2 = map(int, input().split())

# Сортировка сторон первой коробки (без использования списков)
# Находим минимальную, среднюю и максимальную стороны
# Для трех чисел это можно сделать через сравнения

# Для первой коробки
if A1 <= B1 and A1 <= C1:
    min1 = A1
    if B1 <= C1:
        mid1 = B1
        max1 = C1
    else:
        mid1 = C1
        max1 = B1
elif B1 <= A1 and B1 <= C1:
    min1 = B1
    if A1 <= C1:
        mid1 = A1
        max1 = C1
    else:
        mid1 = C1
        max1 = A1
else:  # C1 - минимальная
    min1 = C1
    if A1 <= B1:
        mid1 = A1
        max1 = B1
    else:
        mid1 = B1
        max1 = A1

# Для второй коробки
if A2 <= B2 and A2 <= C2:
    min2 = A2
    if B2 <= C2:
        mid2 = B2
        max2 = C2
    else:
        mid2 = C2
        max2 = B2
elif B2 <= A2 and B2 <= C2:
    min2 = B2
    if A2 <= C2:
        mid2 = A2
        max2 = C2
    else:
        mid2 = C2
        max2 = A2
else:  # C2 - минимальная
    min2 = C2
    if A2 <= B2:
        mid2 = A2
        max2 = B2
    else:
        mid2 = B2
        max2 = A2

# Сравниваем коробки
if min1 == min2 and mid1 == mid2 and max1 == max2:
    print("Boxes are equal")
elif min1 <= min2 and mid1 <= mid2 and max1 <= max2:
    # Проверяем, что хотя бы одно неравенство строгое
    if min1 < min2 or mid1 < mid2 or max1 < max2:
        print("The first box is smaller than the second one")
    else:
        # Если все равны, то это уже обработано выше
        print("Boxes are equal")
elif min2 <= min1 and mid2 <= mid1 and max2 <= max1:
    # Проверяем, что хотя бы одно неравенство строгое
    if min2 < min1 or mid2 < mid1 or max2 < max1:
        print("The first box is larger than the second one")
    else:
        print("Boxes are equal")
else:
    print("Boxes are incomparable")