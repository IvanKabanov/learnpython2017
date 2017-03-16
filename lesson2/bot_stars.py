from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import ephem

#Main function to connect with bot, conecting to bot, wait for messages
def main():
    updater = Updater("348962351:AAG4E77u0gi_xWvwL-7h_FA_-PA2l9AR4LQ")
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("help", help_message))
    dp.add_handler(CommandHandler("planet", planet_constellation, pass_args = True))
    dp.add_handler(MessageHandler([Filters.text], talk_to_me))
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


def get_answer(question):
    answers = {
        'привет': 'И тебе привет!',
        'как дела?': 'Отлично!',
        'до свидания': 'Пока',
        'что делаешь?': 'Отвечаю на глупые вопросы'
        }
    lower_question = question.lower()
    print(answers.get(lower_question, "Don\'t understand you!"))
    return answers.get(lower_question, "Don\'t understand you!")

def talk_to_me(bot, update):
    print(update.message.text)
    bot.sendMessage(update.message.chat_id, get_answer(update.message.text))

def planet_constellation(bot, update, args):
    planet_input = ' '.join(args).capitalize()
    print(planet_input)
    try:
        planet_func = getattr(ephem, planet_input)()
        planet_func.compute()
        planet_answer = ephem.constellation(planet_func)
        bot.sendMessage(update.message.chat_id, text = 'Planet {} in {} now.'.format(planet_input, planet_answer[1]))        
    except AttributeError:
        bot.sendMessage(update.message.chat_id, text = 'Provide planet name in English, please!')


if __name__ == "__main__":
    main()