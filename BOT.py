import telebot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton
from telebot import types
import API_fraz
def bot():


    # получение токена бота
    x = open('API_kluchi.txt', 'r')
    TOKEN = x.readlines()[1]
    TOKEN=TOKEN[11:]
    bot=telebot. TeleBot (TOKEN)

    Help = 'Что бы получить анедот: нажмите на кнопку на клавиатуре анекдот либо напишите в чате "анекдот".\n\nЧто бы получить цитату: нажмите на кнопку на клавиатуре цитата либо напишите в чате "цитата".\n\nДля связи с автором:\ni_dont_now2@mail.ru'

    # создание клавиатуры
    keyboard=ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(KeyboardButton('Цитата'),KeyboardButton('Анекдот'))
    keyboard.add(KeyboardButton('Помощь'))

    @bot.message_handler(commands=['help', 'start']) # начало работы, получение id пользователя
    def send_welcome (message):
        bot.send_message(message.chat.id, Help,reply_markup=keyboard)

    # темы цитат
    c=['любое','age','alone','amazing','anger','architecture','art','attitude','beauty','best','birthday','business','car',
       'change','communications','computers','cool','courage','dad','dating','death','design','dreams','education',
       'environmental','equality','experience','failure','faith','family','famous','fear','fitness','food','forgiveness',
       'freedom','friendship','funny','future','god','good','government','graduation','great','happiness','health',
       'history','home','hope','humor','imagination','inspirational','intelligence','jealousy','knowledge','leadership',
       'learning','legal','life','love','marriage','medical','men','mom','money','morning','movies','success']



    @bot.message_handler(func=lambda s: 'Цитата' in s.text)   # цитата
    def quote(message):
        try:
            @bot.callback_query_handler(func=lambda call: True) #запускается при нажатии на кнопку||||выводит цитату
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

    @bot.message_handler(func=lambda s: 'Помощь' in s.text) # помощь
    def help(message):
        try:
            bot.send_message(message.chat.id, Help)
        except:
            bot.send_message(message.chat.id, 'Непредвиденная ошибка')


    bot.infinity_polling()
if __name__ == '__main__':
    bot()