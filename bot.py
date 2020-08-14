from logging import INFO
from telegram import bot
from telegram.ext import Updater,CommandHandler
import logging

### Import model libraries
import pickle
import tensorflow as tf

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',level=logging.INFO)
updater = Updater(token='1360818300:AAHVIkYmMY-6uA6wvX728RcMem4E6wHgKgY',use_context=True)
dispatcher = updater.dispatcher

def start(update,context):
    context.bot.sendMessage(chat_id=update.effective_chat.id, text='Hello there. How you doin')

def twss(update,context):

    chat_id=update.effective_chat.id
    receive = " ".join(context.args[0:])
    message = str(receive)

    with open("tokenizer_new.pickle", "rb") as handle:
        tokenizer = pickle.load(handle)
    
    model = tf.keras.models.load_model("model-1.h5")

    sequence = tokenizer.texts_to_sequences([message])
    padded_sequence = tf.keras.preprocessing.sequence.pad_sequences(
        sequence,
        maxlen=100,
        padding="post",
        truncating="post"
    )

    pred_score = model.predict(padded_sequence)
    pred_class = (pred_score > 0.5).astype("int32")

    if pred_class:
        print('That is what she said! ;)')
        # context.bot.sendMessage(chat_id=chat_id, text="That's what she said.")
        update.message.reply_html(f'That\'s what she said.\n<code>pred_class: {pred_class}\npred_score: {pred_score}</code>')
        print(f'[INFO] pred_class : {pred_class}')
        print(f'[INFO] pred_score : {pred_score}')
    else:
        print('Not a TWSS punchline! :(')
        print(f'[INFO] pred_class : {pred_class}')
        print(f'[INFO] pred_score : {1.0 - pred_score}')
        update.message.reply_html(f'You gotta be kidding me.\n<code>pred_class: {pred_class}\npred_score: {pred_score}</code>')
        # context.bot.sendMessage(chat_id=chat_id, text="You gotta be kidding me")
    

start_handler = CommandHandler('start',start)
twss_handler = CommandHandler('_',twss)
dispatcher.add_handler(start_handler)
dispatcher.add_handler(twss_handler)

updater.start_polling() 
