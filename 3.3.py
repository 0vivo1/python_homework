#Принимает три позиционных аргумента и выводит сумму двух больших из них
def sum_of_max(x, y, z):
    m = [x, y, z]
    b = m.remove(min(m))
    n = sum(m)
    return n
print(sum_of_max(1, 2, 3))