import telebot
import google.generativeai as genai

# ضع معلوماتك هنا مباشرة
TELEGRAM_TOKEN = "ضع_التوكن_الخاص_بك_هنا"
GEMINI_KEY = "ضع_مفتاح_جيمناي_الخاص_بك_هنا"

bot = telebot.TeleBot(TELEGRAM_TOKEN)
genai.configure(api_key=GEMINI_KEY)
model = genai.GenerativeModel('gemini-pro')

@bot.message_handler(func=lambda message: True)
def chat(message):
    try:
        response = model.generate_content(message.text)
        bot.reply_to(message, response.text)
    except Exception as e:
        bot.reply_to(message, "حدث خطأ، حاول مرة أخرى.")

print("البوت يعمل الآن...")
bot.infinity_polling()
