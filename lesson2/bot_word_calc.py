from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

#Main function to connect with bot, conecting to bot, wait for messages
def main():
    updater = Updater("348962351:AAG4E77u0gi_xWvwL-7h_FA_-PA2l9AR4LQ")
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("help", help_message))
    dp.add_handler(MessageHandler([Filters.text], word_calculator))
    dp.add_error_handler(show_error)
    updater.start_polling()
    updater.idle()

def greet_user(bot, update):
    print('Вызван /start')
    #print(update)
    bot.sendMessage(update.message.chat_id, text='Давай общаться!')

def help_message(bot, update):
    print("Вызван /help")
    bot.sendMessage(update.message.chat_id, text=
        '\n /start - поздороваться'
        '\n/help - вывести это сообщение'
        '\nВведите математическую операцию, например "три плюс два"'
        )

def show_error(bot, update, error):
    print(error)

#def find_calc_operator(found_operator):
#    if 

def word_calculator(bot, update):
    input_text = update.message.text.lower().split()


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
    'поделить': '/',
    'умножить': '*'
    }
        
    #Ищем агрументы
    args_position_list = [] #Создаем список из позиций аргументов в введенном тексте
    for word in integers_words: #
        if word in input_text:
            args_position_list.append(input_text.index(word)) #Добавляем позицию найденного слова в список
            
    if len(args_position_list) != 2: #Если не ДВА аргумента, не работает
        bot.sendMessage(update.message.chat_id, text='Provide TWO arguments')
    else:
        args_position_list.sort() #Сортируем, чтобы выставить аргументы в правильном порядке
        arg1 = integers_words[input_text[args_position_list[0]]]
        arg2 = integers_words[input_text[args_position_list[1]]]
        
        operators_position_list = []
        for operator_string in operators:
            if operator_string in input_text:
                operators_position_list.append(input_text.index(operator_string))
        if len(operators_position_list) != 1: #Оператор должен быть один
            bot.sendMessage(update.message.chat_id, text='Input ONE operator')   
        else:
            operator = operators[input_text[operators_position_list[0]]]
            #Выполняем вычисления    
            if  operator == "+":
                result = arg1 + arg2
            elif operator == "-":
                result = arg1 - arg2    
            elif operator == "*":
                result = arg1 * arg2    
            elif operator == "/":
                if arg2 == 0:
                    bot.sendMessage(update.message.chat_id, text='На ноль делить нельзя')
                result = arg1 / arg2   
            
            bot.sendMessage(update.message.chat_id, text='{}'.format(result))

 
if __name__ == "__main__":
    main()