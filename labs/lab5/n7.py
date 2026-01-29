dict = {'table': 'стол', 'bread': 'хлеб', 'computer': 'компьютер'}
inpt = input("Русское слово: ")
for a, b in dict.items():
    if b==inpt:
        print(a)