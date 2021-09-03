from itertools import count
from math import factorial


def generate_fact():
    for i in count(1):
        yield
        factorial(i)


x = 0
for j in generate_fact():
    if x == 15:
        break
    else:
        x += 1
        print(f'Factorial {x} = {j}')
