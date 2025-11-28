try:

    price = int(input(' Введите сумму покупки: '))
    
    if price < 1000:
        paiement = price
        discount = '0%'
    elif price <= 5000:
        paiement = price - (price * 0.05)
        discount = '5%'
    elif price <= 10000:
        paiement = price - (price * 0.1)
        discount = '10%'
    elif price > 10000:
        paiement = price - (price * 0.15)
        discount = '15'
    print(' Ваша скидка:', discount, '\n', 'К оплате:', paiement)
    
except ValueError:
    print("Ошибка: введите число!")