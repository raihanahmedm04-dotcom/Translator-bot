import telebot
from googletrans import Translator

# তোমার বটের টোকেন
API_TOKEN = "8433316238:AAHNJxtRwwOt2c0LD6U_-O7-xWI9F4mpjyM"
bot = telebot.TeleBot(API_TOKEN)
translator = Translator()

@bot.message_handler(func=lambda message: True)
def translate_message(message):
    text = message.text

    # Detect language
    detected_lang = translator.detect(text).lang

    # Bangla হলে → English, English হলে → Bangla
    if detected_lang == "bn":
        translated = translator.translate(text, src="bn", dest="en").text
    else:
        translated = translator.translate(text, src="en", dest="bn").text

    bot.reply_to(message, translated)

print("✅ Bot is running...")
bot.polling()
