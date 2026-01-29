import random

options = ["камень", "ножницы", "бумага", "ящерица", "спок"]
RandOptions = options[random.randint(0,4)]
inpt = input("Твой вариант - ")
print(f"{inpt} vs {RandOptions}")

if inpt == "ножницы" and RandOptions == "бумага":
    print("Ты победил!")
elif inpt == "бумага" and RandOptions == "камень":
    print("Ты победил!")
elif inpt == "камень" and RandOptions == "ножницы":
    print("Ты победил!")
elif inpt == "ящерица" and RandOptions == "спок":
    print("Ты победил!")
elif inpt == "спок" and RandOptions == "ножницы":
    print("Ты победил!")
elif inpt == "ножницы" and RandOptions == "ящерица":
    print("Ты победил!")
elif inpt == "ящерица" and RandOptions == "бумага":
    print("Ты победил!")
elif inpt == "бумага" and RandOptions == "спок":
    print("Ты победил!")
elif inpt == "спок" and RandOptions == "камень":
    print("Ты победил!")
elif inpt == "камень" and RandOptions == "ящерица":
    print("Ты победил!")
else:
    print("Ты проиграл!")
