from random import randint

my_list = [randint(-10, 10) for _ in range(20)]
new_list = [i for i in my_list if my_list.count(i) == 1]
print(f'Original list {my_list}'\nNo
repeats
list
{new_list})
