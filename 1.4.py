user_num = int(input("Введите число : "))
num_1 = user_num % 10
num_2 = user_num % 100 // 10
while user_num > 0:
    user_num = user_num // 10
    if num_2 >= num_1:
        num_1 = num_2
        num_2 = user_num % 10
    elif num_2 < num_1:
        num_2 = user_num % 10

print(f'Самая большая цифра в числе : {num_1}')
