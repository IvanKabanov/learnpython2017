from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from telegram import replykeyboardmarkup, inlinekeyboardmarkup

#Main function to connect with bot, conecting to bot, wait for messages
def main():
    updater = Updater("348962351:AAG4E77u0gi_xWvwL-7h_FA_-PA2l9AR4LQ")
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("help", help_message))
    dp.add_handler(MessageHandler(Filters.text, calculator))
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
        '\nЗадайте вопрос!'
        )

def show_error(bot, update, error):
    print(error)

#def find_calc_operator(found_operator):
#    if 

def calculator(bot, update):
        
    #print(update.message.text)
    #calc_task_list = []
    #symbol_count = 0
    
    if update.message.text[-1] == "=": #Проверяем пробелы на концах и =
        calc_task = update.message.text[:-1] #Changed from [0:-1]
        #calc_task_list = list(calc_task)
        #for symbol in calc_task:
        #    calc_task_list.append(symbol)
        #    symbol_count = symbol_count + 1
        #    if symbol in ['+', '-', "*", "/"]:
        #        symbol_number = symbol_count - 1
        #        operator = symbol
        if '+' in calc_task:
            operator = '+'
            arg1, arg2 = calc_task.split('+', maxsplit=1)
        elif '-' in calc_task:
            operator = '-'
            arg1, arg2 = calc_task.split('-', maxsplit=1)
        elif '*' in calc_task:
            operator = '*'
            arg1, arg2 = calc_task.split('*', maxsplit=1)
        elif '/' in calc_task:
            operator = '/'
            arg1, arg2 = calc_task.split('/', maxsplit=1)
        else:
            bot.sendMessage(update.message.chat_id, text='No operator found')
        #arg1 = int(calc_task[0:symbol_number])
        #arg2 = int(calc_task[symbol_number+1:])
        arg1 = int(arg1)
        arg2 = int(arg2)
        if operator == "+":
            result = arg1 + arg2
        elif operator == "-":
            result = arg1 - arg2    
        elif operator == "*":
            result = arg1 * arg2    
        elif operator == "/":
            result = arg1 / arg2
        bot.sendMessage(update.message.chat_id, text='{}'.format(result))                
                
        #print(calc_task_list)
             
            

    else:
        bot.sendMessage(update.message.chat_id, text='Main error')            



if __name__ == "__main__":
    main()