item_number = 0
full_list = []
names = []
prices = []
amounts = []
units = []
while True:
    item_number += 1
    name = input("Название: ")
    price = input("Цена: ")
    amount = input("Количество: ")
    unit = input("Единицы измерения: ")
    out = input("Для продолжения введите любой символ, или пустую строку. для выхода введите 0: ")

    data = {'Название': name, 'Цена': price, 'Количество': amount, 'Единицы': unit}
    c_data = (item_number, data)
    full_list.append(c_data)
    names.append(name)
    prices.append(price)
    amounts.append(amount)
    units.append(unit)
    goods = {'Названия : ': names, 'Цены :': prices, 'Количества :': amounts, 'Единицы : ': set(units)}
    if out == '0':
        break
print(full_list)
print(goods)
