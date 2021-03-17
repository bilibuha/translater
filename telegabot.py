import telebot
from google_trans_new import google_translator  

bot = telebot.TeleBot('1645794458:AAEBLOnYuQqH4vZovZpUfYEcfc65V80rQJQ')

translator = google_translator()
detector = google_translator()     

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.send_message(message.chat.id, "*Бот переводит сообщения с любого языка на русский*", parse_mode= "Markdown")

@bot.message_handler(content_types=["text"])

def translate (message): 

    if detector.detect(message.text) == ['ru', 'russian']:
    	bot.send_message(message.chat.id, "*Вы ввели текст на русском, но ладно, всё равно переведу, но только на английский:*\n"+translator.translate(message.text,lang_tgt='en'), parse_mode= "Markdown")
    else:
	    bot.send_message(message.chat.id, translator.translate(message.text,lang_tgt='ru'))

if __name__ == '__main__':
     bot.infinity_polling()