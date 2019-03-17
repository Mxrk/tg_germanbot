from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from Config import token
import logging

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

updater = Updater(token=token)
dispatcher = updater.dispatcher
print("running")


def start(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="hi")


def joinAlert(bot, update):
    for member in update.message.new_chat_members:
        bot.send_message(update.message.chat_id, text="Willkommen " + member.username)
    # logger


def rules(bot, update):
    bot.send_message(update.message.chat_id, text="rules ...")


dispatcher.add_handler(MessageHandler(Filters.status_update.new_chat_members, joinAlert))
dispatcher.add_handler(CommandHandler('start', start))
updater.start_polling()
