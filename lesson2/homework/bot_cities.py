from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from past.builtins import execfile
from cities import cities


#Main function to connect with bot, conecting to bot, wait for messages
def main():
    updater = Updater("348962351:AAG4E77u0gi_xWvwL-7h_FA_-PA2l9AR4LQ")
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("help", help_message))
    dp.add_handler(CommandHandler("goroda", goroda, pass_args = True))
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

#execfile('cities.py')

cities = [element.lower() for element in cities]
response_last_letter = " "

def goroda(bot, update, args):
    global response, cities, response_last_letter 
    input_text = ' '.join(args).lower().strip()
    input_last_letter = input_text[-1]
    city_count = len(cities)
    
    if response_last_letter != input_text[0] and response_last_letter != " ":
        bot.sendMessage(update.message.chat_id, text ='Назовите город на букву {}'.format(response_last_letter.upper()))
        return
    
    if city_count != 0:
        input_city_check = input_text in cities
        if input_city_check == True:
            input_city = cities.pop(cities.index(input_text))
            input_last_letter = input_city[-1]
            
            matches_found = 0
            city_index = 0
                    
            while matches_found < 1 and city_index <= city_count:
                if cities[city_index][0] == input_last_letter:
                    response = cities.pop(city_index)
                    response_last_letter = response[-1]
                    matches_found += 1
                city_index += 1
            if matches_found == 0:
                bot.sendMessage(update.message.chat_id, text ='Не найден город на {}. Просмотрено {} городов. Похоже, Вы выиграли'.format(input_last_letter, city_count))
                return response, cities, response_last_letter
            else:
                bot.sendMessage(update.message.chat_id, text ='{}. Ваш ход'.format(response.capitalize()))
                return response, cities, response_last_letter
            
        else:
            bot.sendMessage(update.message.chat_id, text ='Такой город не найден')
             
    else:
        bot.sendMessage(update.message.chat_id, text ='Cписок городов пуст')


if __name__ == "__main__":
    main()