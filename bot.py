import os
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters

TOKEN = os.getenv("BOT_TOKEN")  # ناخد التوكن من متغير البيئة

# دالة البداية
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        ["سؤالك عن المطور"],
        ["سؤالك عن البوت"],
        ["سؤالك عن كيفية تشغيل البوت"],
        ["سؤالك عن شئ اخر"]
    ]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    await update.message.reply_text(
        "أهلاً وسهلاً بك في Body AI 🤖\nأتمنى لك تجربة سعيدة 🌟",
        reply_markup=reply_markup
    )

# دالة القائمة
async def show_menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        ["سؤالك عن المطور"],
        ["سؤالك عن البوت"],
        ["سؤالك عن كيفية تشغيل البوت"],
        ["سؤالك عن شئ اخر"]
    ]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    await update.message.reply_text("رجعتك للقائمة الرئيسية 👇", reply_markup=reply_markup)

# دالة الرد على الأزرار
async def handle_buttons(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text

    if text == "سؤالك عن المطور":
        await update.message.reply_text(
            "📌 المهندس: عبدالرحمن بلال 👨‍💻\n📞 الموبايل: [اتصل الآن](tel:01558518590)",
            parse_mode="Markdown"
        )
        await update.message.reply_text(
            "⬅️ اضغط رجوع للقائمة",
            reply_markup=ReplyKeyboardMarkup([["رجوع للقائمة"]], resize_keyboard=True)
        )

    elif text == "سؤالك عن البوت":
        await update.message.reply_text("🤖 البوت دا معمول لمساعدتك في الرد على أسئلتك وأي استفسارات تخص استخدامه.")
        await update.message.reply_text(
            "⬅️ اضغط رجوع للقائمة",
            reply_markup=ReplyKeyboardMarkup([["رجوع للقائمة"]], resize_keyboard=True)
        )

    elif text == "سؤالك عن كيفية تشغيل البوت":
        await update.message.reply_text("⚙️ لتشغيل البوت: افتح الرابط واضغط Start.")
        await update.message.reply_text(
            "⬅️ اضغط رجوع للقائمة",
            reply_markup=ReplyKeyboardMarkup([["رجوع للقائمة"]], resize_keyboard=True)
        )

    elif text == "سؤالك عن شئ اخر":
        await update.message.reply_text("📝 من فضلك اكتب سؤالك وسأحاول مساعدتك فيه.")
        await update.message.reply_text(
            "⬅️ اضغط رجوع للقائمة",
            reply_markup=ReplyKeyboardMarkup([["رجوع للقائمة"]], resize_keyboard=True)
        )

    elif text == "رجوع للقائمة":
        await show_menu(update, context)

    else:
        await update.message.reply_text("❓ مش فاهم قصدك، اختار من القايمة أو اكتب استفسارك.")

# main
def main():
    if not TOKEN:
        raise ValueError("⚠️ BOT_TOKEN مش موجود! ضيفه كـ Environment Variable.")

    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_buttons))

    print("🤖 البوت شغال ...")
    app.run_polling()

if __name__ == "__main__":
    main()
