import telebot
import os
from flask import Flask, request
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

@server.route('/' + tokenBot.TOKEN, methods=['POST'])
def getMessage():
    bot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
    return "!", 200

@server.route("/")
def webhook():
    bot.remove_webhook()
    bot.set_webhook(url='https://test-new-new.herokuapp.com/' + tokenBot.TOKEN)
    return "!", 200

if __name__ == '__main__':
     bot.infinity_polling()
     server.debug = True
     server.run(host="0.0.0.0", port=int(os.environ.get('PORT', 5000)))