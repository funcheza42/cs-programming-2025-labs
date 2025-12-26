try:
    
    number = input('Введите три числа через пробел: ')
    a, b, c = number.split()

    if a < b and a < c:
        min = a
    elif b < a and b < c:
        min = b
    else:
        c < a and c < b
        min = c
    print(f"Минимальное число: {min}")
    
except ValueError:
    print("Ошибка: введите число!")