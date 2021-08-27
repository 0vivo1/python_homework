x = float(input())
y = int(input('-'))
def my_func(x, y):
    const_x = x
    for a in range(y - 1):
        x = x * const_x
        print(x)
    res = 1 / x
    return res
print(my_func(x, y))



