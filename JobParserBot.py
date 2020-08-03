import telegram
import logging
from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler, Filters
from yapars import find_vacancies


updater = Updater(token = '1318932508:AAE5l82TDAedYUxSXf0rpAXvzd8d1SwfxOM', use_context = True)
dispatcher = updater.dispatcher

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)

def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text = 'Привет, выбери команду и получишь набор вакансий!' )
    

start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

def django(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text = find_vacancies('django Санкт-Петербург'))
    

django_handler = CommandHandler('django', django)
dispatcher.add_handler(django_handler)

def python(update, context):
    context.bot.send_message(chat_id = update.effective_chat.id, text = find_vacancies('python Санкт-Петербург'))

python_handler = CommandHandler('python', python)
dispatcher.add_handler(python_handler)

def beck(update, context):
    context.bot.send_message(chat_id = update.effective_chat.id, text = Beck())

beck_handler = CommandHandler('beck', beck)
dispatcher.add_handler(beck_handler)

def pyjunior(update, context):
    context.bot.send_message(chat_id = update.effective_chat.id, text = find_vacancies('python junior Санкт-Петербург'))

pyjunior_handler = CommandHandler('pyjunior', pyjunior)
dispatcher.add_handler(pyjunior_handler)

def web(update, context):
    context.bot.send_message(chat_id = update.effective_chat.id, text = find_vacancies('web developer junior Санкт-Петербург'))

web_handler = CommandHandler('web', web)
dispatcher.add_handler(web_handler)

def selo(update, context):
    context.bot.send_message(chat_id = update.effective_chat.id, text = find_vacancies('selenium Санкт-Петербург'))

selo_handler = CommandHandler('selo', selo)
dispatcher.add_handler(selo_handler)

def echo(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)


echo_handler = MessageHandler(Filters.text & (~Filters.command), echo)
dispatcher.add_handler(echo_handler)

updater.start_polling() # - Запуск бота
updater.idle() # - Вырубаем бота


#def caps(update, context):
#    text_caps = ' '.join(context.args).upper()
#    context.bot.send_message(chat_id=update.effective_chat.id, text=text_caps)

#caps_handler = CommandHandler('caps', caps)
#dispatcher.add_handler(caps_handler)


#bot = telegram.Bot(token = '1318932508:AAE5l82TDAedYUxSXf0rpAXvzd8d1SwfxOM')

#print(bot.get_me())