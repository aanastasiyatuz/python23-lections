import telebot
from decouple import config

token = config('TOKEN')
# config - функция, которая достает значение переменной в файле .env (пример, как должен выглядеть файл .env в файле env-example)

bot = telebot.TeleBot(token)

# декоратор message_handler нужен, чтобы реагировать на определенные сообщения
# commands - список команд (функция работает, когда ползователь написал одну из них)
# content_types - список типов сообщений (text, audio, document, photo, sticker, video, video_note, voice, location, contact, new_chat_members, left_chat_member, new_chat_title, new_chat_photo, delete_chat_photo, group_chat_created, supergroup_chat_created, channel_chat_created, migrate_to_chat_id, migrate_from_chat_id, pinned_message, web_app_data)
# content_types=['text'] - функция будет работать, когда пользователь отправил обычное сообщение
# content_types=['audio'] - работает, когда отправил айдио сообщение
# ...
@bot.message_handler(commands=['start', 'hello'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет')
    # отправить текстовое сообщение

    bot.send_sticker(message.chat.id, 'CAACAgQAAxkBAAEGOXZjW12afVYKhgVDsLRI7Ixl3hkl-AACbxcAAqbxcR5QInDpdSq3WyoE')
    # отправить стикер, чтобы получить id стикера @idstickerbot

    bot.send_photo(message.chat.id, 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRw3W4DmK0lYf4sNIMdftQ6I1jQ4KiMP7qOIJCwf2p1&s')
    # отправить фото из ссылки

    with open('./image.jpg', 'rb') as img:
        bot.send_photo(message.chat.id, img)
    # отправить фото с компьютера



bot.polling()
# запуск бота