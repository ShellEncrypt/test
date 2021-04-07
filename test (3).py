import telebot

bot = telebot.TeleBot('1797122575:AAF6U8L8Wpq61p0VnjpSiZ6vSa7rNjVdhd8')

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'hello')

bot.polling()