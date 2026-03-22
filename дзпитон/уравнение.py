# Чтение входных данных
a, b, c = map(int, input().split())

# Случай: a = 0
if a == 0:
    if b == 0:
        if c == 0:
            print(-1)
        else:
            print(0)
    else:
        print(1)
        root = -c / b
        if abs(root) < 1e-10:
            print("0.0000")
        else:
            print("{:.4f}".format(root))

# Случай: a ≠ 0
else:
    D = b * b - 4 * a * c
    
    if D < 0:
        print(0)
    
    elif D == 0:
        print(1)
        root = -b / (2 * a)
        if abs(root) < 1e-10:
            print("0.0000")
        else:
            print("{:.4f}".format(root))
    
    else:
        print(2)
        sqrt_D = D ** 0.5
        
        root1 = (-b - sqrt_D) / (2 * a)
        root2 = (-b + sqrt_D) / (2 * a)
        
        # Сортировка по возрастанию
        if root1 > root2:
            root1, root2 = root2, root1
        
        # Вывод корней
        if abs(root1) < 1e-10:
            print("0.0000")
        else:
            print("{:.4f}".format(root1))
        
        if abs(root2) < 1e-10:
            print("0.0000")
        else:
            print("{:.4f}".format(root2))