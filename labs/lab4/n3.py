try:
    
    age = int(input("возвраст собаки: "))
    
    if age > 0 and age < 23:
        if age == 1 or age == 2:
            age *= 10.5
        else:
            age = age * 4 + 13
    print(f"Возраст собаки в человеческих годах: {age}")
    
except ValueError:
    print("Число надо!")