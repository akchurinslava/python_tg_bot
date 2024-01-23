from pyowm import OWM
from pyowm.utils import config
from pyowm.utils import timestamps
import telebot

owm = OWM('d5666ecdd24c4302ddf8185dde9103cb')
mgr = owm.weather_manager()
bot = telebot.TeleBot("5088860266:AAGdkaA8QPvE4KdF-EPsD3XTbKrapheSPKA")

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Здарова Бякстер любитель, напиши любой город, который хочешь в сообщение, но на английском, например: London")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
        observation = mgr.weather_at_place( message.text)
        w = observation.weather
        tempa=w.temperature('celsius')['temp']
        answer='In town ' + message.text + ' now ' + w.detailed_status +'\n'
        answer+= ('Temperature now about ' + str(tempa)) + '\n\n'
        if tempa<10:
            answer+=('Очень холодно, валяйся на диване')
        elif tempa>10:
            answer+=('Да тоже валяйся на диване')
        elif tempa>20:
            answer+=('Да уже жарко, тоже на диване будь')   
        bot.send_message(message.chat.id, answer)

	
bot.polling(none_stop=True)
