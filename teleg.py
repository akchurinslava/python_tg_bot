import telebot

bot = telebot.TeleBot("5088860266:AAGdkaA8QPvE4KdF-EPsD3XTbKrapheSPKA")

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Здарова Микстерио")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
	bot.send_message(message.chat.id, message.text)

	
bot.polling(none_stop=True)
