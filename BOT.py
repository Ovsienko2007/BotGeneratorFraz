import telebot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton
from telebot import types
import API_fraz

from categories import categories
# список видов цитат
c = categories.cat()

def bot():
    # получение токена бота
    x = open('API_kluchi.txt', 'r')
    TOKEN = x.readlines()[1]
    TOKEN=TOKEN[11:]
    bot=telebot. TeleBot (TOKEN)

    H = ['Что бы получить анедот: нажмите на кнопку на клавиатуре анекдот либо напишите в чате "анекдот".',
            'Что бы получить цитату: нажмите на кнопку на клавиатуре цитата либо напишите в чате "цитата".',
            'Для связи с автором:',
            'i_dont_now2@mail.ru']
    Help=str('\n\n'.join(H))

    # создание клавиатуры
    keyboard=ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(KeyboardButton('Цитата'),KeyboardButton('Анекдот'))
    keyboard.add(KeyboardButton('Помощь'))

    # начало работы, получение id пользователя
    @bot.message_handler(commands=['help', 'start'])
    def send_welcome (message):
        bot.send_message(message.chat.id, Help,reply_markup=keyboard)

    # цитата
    @bot.message_handler(func=lambda s: 'Цитата' in s.text)
    def quote(message):
        try:
            @bot.callback_query_handler(func=lambda call: True) #запускается при нажатии на кнопку и выводит цитату
            def callback_inline(call):
                bot.send_message(message.chat.id, API_fraz.quotes(call.data))

            # сборка клавиатуры из кнопок
            markup = types.InlineKeyboardMarkup()
            for i in c:
                markup.add(types.InlineKeyboardButton(i, callback_data=i))

            bot.send_message(message.chat.id,"Выбери тему цитаты".format(message.from_user),reply_markup=markup)
        except:
            bot.send_message(message.chat.id, 'Непредвиденная ошибка')

    @bot.message_handler(func=lambda s: 'Анекдот' in s.text) # анекдот
    def anekdot(message):
        try:
            bot.send_message(message.chat.id, API_fraz.anekdot())
        except:
            bot.send_message(message.chat.id, 'Непредвиденная ошибка')

    # помощь
    @bot.message_handler(func=lambda s: 'Помощь' in s.text)
    def help(message):
        try:
            bot.send_message(message.chat.id, Help)
        except:
            bot.send_message(message.chat.id, 'Непредвиденная ошибка')


    bot.infinity_polling()
if __name__ == '__main__':
    bot()