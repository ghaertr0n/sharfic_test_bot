from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import misc, weather
updater = Updater(token=misc.token) # Токен API к Telegram
dispatcher = updater.dispatcher

def startCommand(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text='Привет, пиши')

def textMessage(bot, update):

    answer = update.message.text
    astana_temp = weather.get_weather()

    if answer == 'а что реализовано?':
        bot.send_message(chat_id=update.message.chat_id, text='Только погода в Астане :D')
    elif answer == 'погода':
        bot.send_message(chat_id=update.message.chat_id, text=astana_temp)
    else:
        bot.send_message(chat_id=update.message.chat_id, text='Распознавание этого во мне пока не реализовано')

start_command_handler = CommandHandler('start', startCommand)
text_message_handler = MessageHandler(Filters.text, textMessage)

dispatcher.add_handler(start_command_handler)
dispatcher.add_handler(text_message_handler)

updater.start_polling(clean=True)

updater.idle()
