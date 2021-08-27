def division_func(num1 = float(input("Делимое : ")), num2 = float(input("Делитель : "))):
    try:
        return num1 / num2
    except ZeroDivisionError:
        return "На ноль делить нельзя"

print(division_func())