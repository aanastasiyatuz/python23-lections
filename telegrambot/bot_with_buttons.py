import telebot
from decouple import config

token = config('TOKEN')

bot = telebot.TeleBot(token)

# клавиатура, которая будет находиться там, где клавиатура
keyboard = telebot.types.ReplyKeyboardMarkup()
button1 = telebot.types.KeyboardButton('Да')
button2 = telebot.types.KeyboardButton('Нет')
keyboard.add(button1, button2)

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет, выбери кнопку', reply_markup=keyboard)
    # register_next_step_handler принимает сообщение и функцию, которая фызовется как только позователь отправит любое сообщение
    # это сообщение и передастся в функцию
    bot.register_next_step_handler(message, reply_to_button)

def reply_to_button(message):
    if message.text == 'Да':
        bot.send_sticker(message.chat.id, 'CAACAgQAAxkBAAEGOodjW2mCpdnkWm7-6YIAAZcRWB-V3U4AAkMJAAKWnflRZ91LE87yDQ8qBA')
    elif message.text == 'Нет':
        bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAEGOqVjW2m8qpmg5eTUxCebGduCfL5GegACeRcAAvRKAUsu7NezbSnhtioE')
    else:
        bot.send_message(message.chat.id, 'Нажмите на кнопку')
        bot.register_next_step_handler(message, reply_to_button)

bot.polling()