import telebot
from decouple import config

token = config('TOKEN')

bot = telebot.TeleBot(token)

# клавиатура, которая будет прикреплена под сообщением
# при нажатии на кнопку будет искаться функция, задекорированная callback_query_handler
keyboard = telebot.types.InlineKeyboardMarkup()
button1 = telebot.types.InlineKeyboardButton('Да', callback_data='yes')
button2 = telebot.types.InlineKeyboardButton('Нет', callback_data='no')
keyboard.add(button1, button2)

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет, выбери кнопку:', reply_markup=keyboard)

# func - функция-фильтр, в данном случае мы возвращаем True, пропуская все сообщения
@bot.callback_query_handler(func=lambda x: True)
def reply_to_button(call):
    # call.data - будет занчение callback_data из нажатой кнопки
    if call.data == 'yes':
        bot.send_sticker(call.from_user.id, 'CAACAgQAAxkBAAEGOodjW2mCpdnkWm7-6YIAAZcRWB-V3U4AAkMJAAKWnflRZ91LE87yDQ8qBA')
    elif call.data == 'no':
        bot.send_sticker(call.from_user.id, 'CAACAgIAAxkBAAEGOqVjW2m8qpmg5eTUxCebGduCfL5GegACeRcAAvRKAUsu7NezbSnhtioE')


bot.polling()