best_name = ""
best_avg = 0
students = [("Анна", [5, 5, 5]), ("Иван", [3, 4, 4]), ("Мария", [5, 4, 5])]

for name, marks in students:
    total = 0
    for mark in marks:
        total += mark
    avg = total / len(marks)
    
    if avg > best_avg:
        best_avg = avg
        best_name = name

print(best_name, best_avg)