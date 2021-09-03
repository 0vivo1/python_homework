from itertools import count, cycle

my_count = count(10)
my_cycle = cycle("ASDFGH")

for _ in range(5):
    print('(my_count, my_cycle) = ({}, {})'.format(next(my_count), next(my_cycle)))
