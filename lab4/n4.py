number = input("Ввкдите число: ")
last = int(number[-1])

if last % 2 == 0 and int(number) % 3 == 0:
    print("число делится на 6")
else:
    print("число не делится на 6")