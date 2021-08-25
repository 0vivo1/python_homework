user_input = input()
user_list = user_input.split(' ')
str_num = 0
for unit in user_list:
    str_num += 1
    print(f'{str_num}  {unit:.10}')