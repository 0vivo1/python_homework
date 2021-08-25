user_input = input('Введите значения через пробел  ')
exchange_list = user_input.split(' ')
l = len(exchange_list) - 1
i = 0
while i < l:
    j = i + 1
    exchange_list[i], exchange_list[j] = exchange_list[j], exchange_list[i]
    i = i + 2
print(exchange_list)
