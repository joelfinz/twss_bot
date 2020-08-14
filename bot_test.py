from telegram.ext import Updater,CommandHandler
import logging

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',level=logging.INFO)
updater = Updater(token='1360818300:AAHVIkYmMY-6uA6wvX728RcMem4E6wHgKgY',use_context=True)
dispatcher = updater.dispatcher

def start(update,context):
    context.bot.sendMessage(chat_id=update.effective_chat.id, text='Hello there. How you doin')
    
    
def twss(update,context):
    chat_id=update.effective_chat.id
    receive = " ".join(context.args[0:])
    message = str(receive)
    update.message.reply_text('That is hard man.')
    # context.bot.sendMessage(chat_id=chat_id, text="That's what she said.")
start_handler = CommandHandler('start',start)
twss_handler = CommandHandler('_',twss)
dispatcher.add_handler(start_handler)
dispatcher.add_handler(twss_handler)

updater.start_polling() 