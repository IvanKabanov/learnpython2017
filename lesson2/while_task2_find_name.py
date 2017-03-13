names_list = ["Вася", "Маша", "Петя", "Валера", "Саша", "Даша"]

def find_person(name):
    while names_list[0] != str(name):
        names_list.pop(0)


find_person('Петя')
print("{} нашелся!".format(names_list[0]))
    
