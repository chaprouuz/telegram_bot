from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, ContextTypes, filters
from datetime import datetime, time

TOKEN = '8292170641:AAEalp6IFLdTaFkreglE5R5WFN6G69Xr-uA'

# پیام پاسخ خودکار
OFF_HOURS_MESSAGE = """📌 کاربر گرامی، وقت شما بخیر  
ساعات پاسخ‌گویی *مجتمع چاپ دیجیتال روز* از ساعت *۸ صبح تا ۵ عصر* می‌باشد.  
در حال حاضر، خارج از ساعات کاری هستیم؛ اما پیام شما با دقت ثبت شده و همکاران ما در اولین فرصت در ساعات کاری به آن پاسخ خواهند داد.  
از همراهی شما سپاسگزاریم. 🌺"""

# تابع بررسی ساعات کاری
def is_off_hours():
    now = datetime.now().time()
    start = time(8, 0)   # 8:00 صبح
    end = time(17, 0)    # 5:00 عصر
    return not (start <= now <= end)

# پاسخ به پیام‌ها
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if is_off_hours():
        await update.message.reply_text(OFF_HOURS_MESSAGE, parse_mode="Markdown")

# اجرای ربات
if __name__ == '__main__':
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    print("🤖 ربات فعال شد...")
    app.run_polling()
