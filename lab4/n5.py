pasw = input("Введите пароль английскими буквами: ")

if len(pasw) >= 8:
    if "A" in pasw or "B" in pasw or "C" in pasw or "D" in pasw or "E" in pasw or "F" in pasw or "G" in pasw or "H" in pasw or "I" in pasw or "J" in pasw or "K" in pasw or "L" in pasw or "M" in pasw or "N" in pasw or "O" in pasw or "P" in pasw or "Q" in pasw or "R" in pasw or "S" in pasw or "T" in pasw or "U" in pasw or "V" in pasw or "W" in pasw or "X" in pasw or "Y" in pasw or "Z" in pasw:
        if "a" in pasw or "b" in pasw or "c" in pasw or "d" in pasw or "e" in pasw or "f" in pasw or "g" in pasw or "h" in pasw or "i" in pasw or "j" in pasw or "k" in pasw or "l" in pasw or "m" in pasw or "n" in pasw or "o" in pasw or "p" in pasw or "q" in pasw or "r" in pasw or "s" in pasw or "t" in pasw or "u" in pasw or "v" in pasw or "w" in pasw or "x" in pasw or "y" in pasw or "z" in pasw:
            if "0" in pasw or "1" in pasw or "2" in pasw or "3" in pasw or "4" in pasw or "5" in pasw or "6" in pasw or "7" in pasw or "8" in pasw or "9" in pasw:
                if "!" in pasw or "@" in pasw or "#" in pasw or "$" in pasw or "%" in pasw or "^" in pasw or "&" in pasw or "*" in pasw or "(" in pasw or ")" in pasw or "-" in pasw or "_" in pasw or "=" in pasw or "+" in pasw or "{" in pasw or "}" in pasw or "[" in pasw or "]" in pasw or ":" in pasw or ";" in pasw or '\\' in pasw or "'" in pasw or "<" in pasw or ">" in pasw or "," in pasw or "." in pasw or "?" in pasw or "/" in pasw or "~" in pasw or "`" in pasw:
                    print('подходит')
            else:
                print("пароль должен состоять из 8 или более символов и должен содержать: заглавные буквы, строчные буквы, числа и специальные символы")
        else:
            print("пароль должен состоять из 8 или более символов и должен содержать: заглавные буквы, строчные буквы, числа и специальные символы")
    else:
        print("пароль должен состоять из 8 или более символов и должен содержать: заглавные буквы, строчные буквы, числа и специальные символы")              
else:
    print('пароль должен состоять из 8 или более символов и должен содержать: заглавные буквы, строчные буквы, числа и специальные символы')