# def one():
#     prices = {'водичка': 50, 'хлебушек': 80, 'салат_айсберг': 200}
#     cheapest = (min(prices.keys()))
#     print(cheapest)
# one()

# def two():
#     prices = {'водичка': 50, 'хлебушек': 80, 'салат_айсберг': 200}
#     cheapest = min(prices, key=prices.get)
#     print("Самый дешевый товар:", cheapest)
# two()

# def three():
#     prices = {'водичка': [20, 30, 40], 'хлебушек': [60, 70, 80], 'салат_айсберг': 200}
#     print(min(prices.get('хлебушек')))
# three()

# def four():
#     prices = {'водичка': 50, 'хлебушек': 80, 'салат_айсберг': 200}
#     print(prices.values())
# four()


prices = {'водичка': 50, 'хлебушек': 80, 'салат_айсберг': 200}
least = min(prices, key=prices.get)
most = max(prices, key=prices.get)
print(f'дешевый товар - {least}\nдорогой товар - {most}')