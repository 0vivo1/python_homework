first = open("first_file.txt", "a", encoding="utf-8")

while True:
    data = input()
    if data != "":
        first.write(f"{data} \n")
    else:
        break
first.close()

