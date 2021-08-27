def sum_all(string):
    final = 0
    nums_list = string.split()
    for i in nums_list:
        try:
            i = int(i)
            final += i
        except ValueError:
            print("Затесалось что-то не то(")
            break
    return final

res = 0
out = 0
while out != 'q':
    nums = input("Ваша сторока из цифр : ")
    res += sum_all(nums)
    print(res)
    out = input('Если не хотите продолжать - введите "q"')








