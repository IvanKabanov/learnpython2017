def word_calculator():
    input_text = input('Ввод: ').split()
    integers_words = {
    "ноль": 0,
    "один": 1,
    "два": 2,
    "три": 3,
    "четыре": 4,
    "пять": 5,
    "шесть": 6,
    "семь": 7,
    "восемь": 8,
    "девять": 9,
    "десять": 10
    }
    
    operators = {
    'плюс': '+',
    'минус': '-',
    'разделить': '/',
    'умножить': '*'
    }
    print(input_text)
    
    #Ищем агрументы
    args_position_list = [] #Создаем список из позиций аргументов в введенном тексте
    for word in integers_words: #
        if word in input_text:
            print(input_text.index(word))
            args_position_list.append(input_text.index(word)) #Добавляем позицию найденного слова в список
            print(args_position_list)
    if len(args_position_list) != 2: #Если не ДВА аргумента, не работает
        print('Provide TWO arguments')
    else:
        args_position_list.sort() #Сортируем, чтобы выставить аргументы в правильном порядке
        arg1 = integers_words[input_text[args_position_list[0]]]
        arg2 = integers_words[input_text[args_position_list[1]]]
        print(arg1,arg2)
        operators_position_list = []
        for operator_string in operators:
            if operator_string in input_text:
                operators_position_list.append(input_text.index(operator_string))
                print(operators_position_list)
        if len(operators_position_list) != 1: #Оператор должен быть один
            print('Input ONE operator')
        else:
            operator = operators[input_text[operators_position_list[0]]]
            print(operator)
        #Выполняем вычисления    
            if  operator == "+":
                result = arg1 + arg2
            elif operator == "-":
                result = arg1 - arg2    
            elif operator == "*":
                result = arg1 * arg2    
            elif operator == "/":
                result = arg1 / arg2   

            print(result)      
    
        
       
            
            
                


word_calculator()