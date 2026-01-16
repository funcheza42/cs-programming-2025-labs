try:
    
    temp = int(input("Введите температуру: "))
    
    if temp >= 20:
        print("Кондиционер выключен")
    else:
        print("Кондиционер включен")
          
except ValueError:
    print("Просили ввести число!")