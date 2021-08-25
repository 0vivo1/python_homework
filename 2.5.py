rate_list = [9, 8, 8, 7, 5, 4, 4, 3]
new_num = int(input())
x = len(rate_list)
for i in rate_list[::-1]:
    if new_num <= i:
        rate_list.insert(x, new_num)
        break
    elif new_num > rate_list[0]:
        rate_list.insert(0, new_num)
    else:
        x -=x
print(rate_list)
