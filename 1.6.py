a = int(input('Километров в первый день : '))
b = int(input('Результат :'))
day = 1
while a < b:
    a = a + a / 10
    day += 1
print(f'Ответ : на {day}-й день результат составил не менее {b} километров')
