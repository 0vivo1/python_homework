units = open("third.txt", "r", encoding="utf-8")
content = units.readlines()
sum = 0
for unit in content:
    unit_list = unit[:-1].split()
    sum += float(unit_list[-1]) / len(content)
    if float(unit_list[-1]) < 20000:
        print(unit_list[0])

print(f'Средняя сумма дохода сотрудников: {sum}')
units.close()