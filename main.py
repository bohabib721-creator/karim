import telebot
import google.generativeai as genai
import os
import http.server
import socketserver
import threading

# الإعدادات - تم تحديثها بمفاتيحك الجديدة
TELEGRAM_TOKEN = "8772903016:AAHAjzCH2iQ5mDH3OGVEsGE8LCPB9Zc0iXM"
GEMINI_API_KEY = "AIzaSyDO-EHfb083eyuC04B8r1duQY556sshUs8"

# تشغيل سيرفر وهمي لإرضاء Render ومنع خطأ Port
def run_dummy_server():
    port = int(os.environ.get("PORT", 8080))
    handler = http.server.SimpleHTTPRequestHandler
    with socketserver.TCPServer(("", port), handler) as httpd:
        print(f"Serving on port {port}")
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
        print(f"Error: {e}")
        bot.reply_to(message, "أنا أعمل، ولكن هناك مشكلة في الاتصال بذكاء جوجل.")

print("Bot is starting...")
bot.infinity_polling()
