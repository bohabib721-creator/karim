import telebot
import google.generativeai as genai

# الإعدادات
TELEGRAM_TOKEN = 8772903016:AAH6o2Y_e8ntazvJhqzEqgQGGgV0vejugdQ
GEMINI_API_KEY = "AIzaSyB..."

# إعداد Gemini
genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel('gemini-pro')

bot = telebot.TeleBot(TELEGRAM_TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "أهلاً كريم! أنا بوت الذكاء الاصطناعي الخاص بك. كيف يمكنني مساعدتك اليوم؟ ⚪️🔥")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    try:
        response = model.generate_content(message.text)
        bot.reply_to(message, response.text)
    except Exception as e:
        bot.reply_to(message, "حدث خطأ بسيط، تأكد من مفتاح Gemini الخاص بك.")

print("البوت يعمل الآن...")
bot.infinity_polling()
