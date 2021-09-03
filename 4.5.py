from functools import reduce


def list_multiplier(x_1, x_2):
    return x_1 * x_2


new_list = [x for x in range(100, 1001, 2)]
print(f"Original list {new_list}\nMultiplication {reduce(list_multiplier, new_list)}")
