# функция должна принимать Имя, Фамилию, год рождения, емеил, телефон как именованные аргументы.
# Потом выводить их одной строкой
def user_data(**kvargs):
    data = ' '.join(list(kvargs.values()))
    return data


print(user_data(name = input(), surname = input(), age = input(), email= input(), phone = input()))