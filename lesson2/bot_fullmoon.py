from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

import ephem, datetime

#Main function to connect with bot, conecting to bot, wait for messages
def main():
    updater = Updater("348962351:AAG4E77u0gi_xWvwL-7h_FA_-PA2l9AR4LQ")
    dp = updater.dispatcher
    dp.add_handler(MessageHandler([Filters.text], next_fullmoon))
    dp.add_error_handler(show_error)
    updater.start_polling()
    updater.idle()

def show_error(bot, update, error):
    print(error)

def next_fullmoon(bot, update):
    input_string = update.message.text.lower()
    if input_string[-1] == '?':
        input_string = input_string[0:-1]
    if input_string[0:33] == 'когда ближайшее полнолуние после ':
        input_string = input_string[33:]
    

    try:
        date_check = datetime.date(int(input_string[0:4]), int(input_string[5:7]), int(input_string[8:]))
        bot.sendMessage(update.message.chat_id, text = 'Следующее полнолуние после {}:  {}'.format(input_string, ephem.next_full_moon(input_string)))
    except (ValueError, TypeError):
        bot.sendMessage(update.message.chat_id, text = 'Пример: Когда ближайшее полнолуние после 2016-10-01?')        



if __name__ == "__main__":
    main()