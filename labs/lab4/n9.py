try:
    
    hour = int(input("Введите час (0-23): "))
    
    if 0 <= hour <= 5:
        time = "ночь"
    elif 6 <= hour <= 11:
        time = "утро"
    elif 12 <= hour <= 17:
        time = "день"
    elif 18 <= hour <= 23:
        time = "вечер"
    else:
        print("Некорректный ввод")
    print("Cейчас", time)
    
except ValueError:
    print("Ошибка: введите число!")