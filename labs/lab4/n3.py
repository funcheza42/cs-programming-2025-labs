try:
    
    age = int(input("возраст собаки: "))
    
    if age > 0 and age < 23:
        if age == 1 or age == 2:
            age *= 10.5
        else:
            age = age * 10.5 + (age - 2) * 8
    print(f"Возраст собаки в человеческих годах: {age}")
    
except ValueError:
    print("Число надо!")

