second = open("second_file.txt", "r", encoding ="utf-8")
s = second.readlines()
print(len(s), "строк(и)")
count = 0
for string in s:
    count += 1
    words = len(string.split(' '))
    print(f'{count}-я стрка:{words} слов(а)')