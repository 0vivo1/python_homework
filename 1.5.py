revenue = int(input("Выручка фирмы : "))
costs = int(input("Издержки фирмы : "))
profit = revenue - costs
if profit > 0:
    print("Фирма приносит прибыль")
    print('Рентабельность составила ', profit / revenue)
else:
    print("Фирма убыточна")
units = int(input("Количество сотрудников : "))
print('Прибыль в расчете на сотрудника составляет ', profit / units)
