mounth_num = int(input('Номер месяца (1-12) : '))
seasons = {
    (1, 2, 12) : 'Winter',
    (3, 4, 5) : 'Spring',
    (6, 7, 8) : 'Summer',
    (9, 10, 11) : 'Autumn'
}
for i in seasons.keys():
    if mounth_num in i:
        print(seasons.get(i))