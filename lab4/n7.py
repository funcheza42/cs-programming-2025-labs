try:
    
    number = input('Введите число: ')
    a, b, c = number.split(' ')

    if a < b and a < c:
        min = a
    elif b < a and b < c:
        min = b
    elif c < a and c < b:
        min = c
    print(min)
    
except ValueError:
    print("Ошибка: введите число!")