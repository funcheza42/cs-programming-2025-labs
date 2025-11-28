try:
    
    temp = int(input("Введите температуру: "))
    
    if temp >= 20:
        print("Кондиционер включен")
    else:
        print("Кондиционер выключен")
          
except ValueError:
    print("Просили ввести число!")