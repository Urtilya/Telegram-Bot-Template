import telebot

with open('TOKEN.txt','r') as file:
	token = file.read()

bot = telebot.TeleBot(token.strip())

#Это тестовый Эхо бот

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to("Это тестовый эхо-бот")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
	bot.reply_to(message, message.text)

bot.polling(non_stop=True)
