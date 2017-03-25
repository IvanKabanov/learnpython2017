from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import ephem

#Main function to connect with bot, conecting to bot, wait for messages
def main():
    updater = Updater("348962351:AAG4E77u0gi_xWvwL-7h_FA_-PA2l9AR4LQ")
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("help", help_message))
    dp.add_handler(CommandHandler("wordcount", word_count, pass_args = True))
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
    print(answers.get(lower_question, "Don't understand you!"))
    return answers.get(lower_question, "Don't understand you!")

def talk_to_me(bot, update):
    print(update.message.text)
    bot.sendMessage(update.message.chat_id, get_answer(update.message.text))

def word_count(bot, update, args):
    word_input = ' '.join(args)
    print(args)
    if word_input == "": #Пустая строка
        bot.sendMessage(update.message.chat_id, text="No arguments passed")
    
    elif word_input[0] == '"' and word_input[-1] == '"': #Проверка кавычек
        if len(word_input) == 2: #проверка если только кавычки
            bot.sendMessage(update.message.chat_id, text="Incorrect input")
        else:    
            print(word_input)
            word_list = word_input[1:-1].strip().split()
            print(word_list)
            bot.sendMessage(update.message.chat_id, text='{}'.format(len(word_list)))
    else:
        print("Something wrong")
        bot.sendMessage(update.message.chat_id, text="Incorrect input_else")    
    #print(word_input)
    

if __name__ == "__main__":
    main()