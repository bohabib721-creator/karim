import telebot
import google.generativeai as genai
import os
import http.server
import socketserver
import threading

# الإعدادات
TELEGRAM_TOKEN = "8772903016:AAFXyO02KJ5w8ZcTepJHrDQnpY0R2LMj7Mo"
GEMINI_API_KEY = "ضعهنا_مفتاح_جوجل_الخاص_بك"

# تشغيل سيرفر وهمي لإرضاء Render ومنع خطأ Port
def run_dummy_server():
    port = int(os.environ.get("PORT", 8080))
    handler = http.server.SimpleHTTPRequestHandler
    with socketserver.TCPServer(("", port), handler) as httpd:
        httpd.serve_forever()

threading.Thread(target=run_dummy_server, daemon=True).start()

# إعداد Gemini
genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel('gemini-pro')
bot = telebot.TeleBot(TELEGRAM_TOKEN)

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    try:
        response = model.generate_content(message.text)
        bot.reply_to(message, response.text)
    except Exception as e:
        bot.reply_to(message, "البوت يعمل ولكن حدث خطأ في التواصل مع ذكاء جوجل.")

bot.infinity_polling()
