all_numbers = None
typl = (15, 6, 4, 1, 7)

for value in typl:
    if type(value) == str:
        all_numbers = False
        break
    elif type(value) == int:
        all_numbers = True
        
if all_numbers:
    print(tuple(sorted(typl)))
else:
    print(typl)
