lst = [6, 'da', 'net', '7']
dicti = {}
for i in lst:
    dicti[str(i)]= i
print(dicti)


elements = ["apple", 42, 3.14, True, "hello"]
result_dict = {str(element): element for element in elements}
print(result_dict)