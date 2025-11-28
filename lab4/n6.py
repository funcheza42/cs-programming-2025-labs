try:
    
    year = int(input("Ввкдите год: "))

    if year % 4 == 0:
        if year % 100 != 0 or year % 400 == 0:
            print("Високосный год")
        else:
            print("Не високосный год")
    else:
        print("Не високосный год")
        
except ValueError:
    print("Ошибка: введите число!")