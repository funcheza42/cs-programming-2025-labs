n = int(input('число: '))
a, b = 0, 1
while a < n:
    print(a)
    # a, b = b, a + b
    c = a + b
    a = b
    b = c
    