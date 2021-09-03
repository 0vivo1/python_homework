
from sys import argv

name, arg_1, arg_2, arg_3 = argv

def the_salary(hours, money_per_hour, bonus):
    try:
        final = int(hours) * int(money_per_hour) + int(bonus)
        return f"Зарплата составила {final}"
    except ValueError:
        return "Вы должны вводить только числа"
print(the_salary(arg_1, arg_2, arg_3))