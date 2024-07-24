from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
import logging
from . import commands
from .config import TOKEN

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)

updater = None

def setup_bot():
    global updater
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", commands.start))
    dp.add_handler(CommandHandler("help", commands.help_command))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, commands.echo))

def start_bot():
    if updater is None:
        setup_bot()
    updater.start_polling()

def stop_bot():
    if updater is not None:
        updater.stop()

def send_message(chat_id, text):
    if updater is not None:
        updater.bot.send_message(chat_id=chat_id, text=text)

if __name__ == '_main_':
    setup_bot()
    start_bot()
    updater.idle()