
try:
    user_age = float(input("Введите свой возраст: "))
    #print("You entered {}".format(user_age))

    if user_age <= 6:
        print("Детский сад")
    elif user_age <= 16:
        print("Школа")
    elif user_age <= 22:
        print("ВУЗ")
    elif user_age <= 100:
        print("Работа")
    else:
        print("You should be dead...")

except ValueError:
        print("Пожалуйта, введите возраст корректно")