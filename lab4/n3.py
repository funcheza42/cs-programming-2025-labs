try:
    
    age = int(input("возвраст собаки: "))
    
    if age >= 1:
        age *= 7
    print(f"Возраст собаки в человеческих годах: {age}")
    
except ValueError:
    print("Число надо!")
    
