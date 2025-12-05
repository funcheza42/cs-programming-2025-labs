try:
    
    number = int(input("Введите число: "))
    
    if number % 2 == 0:
        print(number, "- составное число")
    else:
        print(number, "- простое число")
    
except ValueError:
    print("Ошибка: введите число!")

