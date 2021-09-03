my_list = [300, 2, 12, 144, 1, 1, 4, 10, 7, 1, 78, 123, 55]
bigger_units = [my_list[unit] for unit in range(1, len(my_list)) if my_list[unit] > my_list[unit - 1]]
print(bigger_units)
