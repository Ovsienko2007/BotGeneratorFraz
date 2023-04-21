import telebot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton
import API_fraz
with API_keys
TOKEN= '6080106986:AAFvTaiqrXCECEnFPRuanKPNaEIWxpQgKU8'
bot=telebot. TeleBot (TOKEN)

keyboard=ReplyKeyboardMarkup(resize_keyboard=True)
keyboard.add(KeyboardButton('Цитата'))
keyboard.add(KeyboardButton('Анекдот'))
@bot.message_handler(commands=['help', 'start'])
def send_welcome (message):
    bot.send_message(message.chat.id, 'Я TеCтовый бот!', reply_markup=keyboard)



@bot.message_handler(func=lambda s: 'Цитата' in s.text)
def say_hello(message):
    try:
        bot.send_message(message.chat.id, API_fraz.quotes())
    except:
        bot.send_message(message.chat.id, 'Непредвиденная ошибка')

@bot.message_handler(func=lambda s: 'Анекдот' in s.text)
def echo_message(message):
    try:
        bot.send_message(message.chat.id, API_fraz.anekdot())
    except:
        bot.send_message(message.chat.id, 'Непредвиденная ошибка')


bot.infinity_polling()

