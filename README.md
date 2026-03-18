# 🤖 بوت Telegram ذكاء اصطناعي (Gemini AI Bot)

بوت ذكي يستخدم Google Gemini AI للرد على الرسائل عبر Telegram.

## ✨ الميزات

- 🤖 رد ذكي باستخدام Google Gemini
- 📝 حفظ سجل المحادثات لكل مستخدم
- 🛡️ معالجة متقدمة للأخطاء
- 🔐 حماية المفاتيح في ملف .env
- 📊 نظام تسجيل (Logging)
- ⚡ أوامر خاصة (/start, /help, /clear)
- 📏 حد أقصى للرسائل لتجنب الأخطاء

## 🚀 الإعداد السريع

### 1. تثبيت المتطلبات
```bash
pip install -r requirements.txt
```

### 2. إنشاء ملف .env
```bash
# انسخ المثال
cp .env .env

# ثم عدّل المفاتيح الخاصة بك
TELEGRAM_TOKEN=your_token_here
GEMINI_API_KEY=your_api_key_here
```

### 3. تشغيل البوت
```bash
python main.py
```

## 📋 الأوامر المتاحة

| الأمر | الوصف |
|------|-------|
| `/start` | معلومات الترحيب |
| `/help` | شرح الأوامر المتاحة |
| `/clear` | حذف سجل المحادثات |

## 🔐 معل��مات الأمان

⚠️ **هام جداً:**
- لا تضع المفاتيح في الكود أبداً
- استخدم ملف `.env` فقط
- ملف `.env` مخفي من Git (موجود في `.gitignore`)
- إذا تم رفع المفاتيح بالخطأ، غيّرها فوراً من Google و Telegram

## 📁 هيكل المشروع

```
karim/
├── main.py           # ملف البوت الرئيسي
├── requirements.txt  # المتطلبات
├── .env             # متغيرات البيئة (مخفي من Git)
├── .gitignore       # ملفات مخفية من Git
└── README.md        # هذا الملف
```

## 🛠️ المتطلبات

- Python 3.8+
- Telegram Bot Token
- Google Gemini API Key

احصل عليها من:
- [Telegram BotFather](https://t.me/botfather)
- [Google AI Studio](https://makersuite.google.com/app/apikey)

## 📝 أمثلة الاستخدام

```
المستخدم: /start
البوت: مرحباً! أنا بوت ذكي يستخدم Google Gemini...

المستخدم: مرحباً كيف حالك؟
البوت: مرحباً! أنا بوت ذكي...

المستخدم: /clear
البوت: تم حذف سجل المحادثات الخاص بك.
```

## ⚙️ الإعدادات

يمكنك تعديل ا��إعدادات في `main.py`:

```python
MAX_MESSAGE_LENGTH = 4000  # الحد الأقصى للرسائل
MODEL_NAME = 'gemini-pro'  # نموذج Gemini
```

## 🐛 استكشاف الأخطاء

إذا حدثت مشاكل:

1. تأكد من تثبيت المتطلبات:
   ```bash
   pip install -r requirements.txt
   ```

2. تأكد من ملف `.env` صحيح:
   ```bash
   cat .env
   ```

3. تحقق من سجلات الأخطاء في `bot.log`

## 📞 الدعم

للمساعدة، راجع السجلات في `bot.log`

---

**مصنوع بـ ❤️ باستخدام Python و Gemini AI**