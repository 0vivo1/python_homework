
def int_func(text = input()):
    text_list = text.split()
    final = []
    for i in text_list:
        up_first = i.capitalize()
        final.append(up_first)
    return ' '.join(final)
print(int_func())