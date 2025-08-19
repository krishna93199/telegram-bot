import asyncio
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.constants import ChatAction, ParseMode
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

BOT_TOKEN = "8296566949:AAGBpgUV-pB-qlHj15cWwKVBoHp0TGrH1xU"

# Channels list
CHANNELS = [
    ("Channel 1", "https://t.me/+EtDaG5R8bJtjNDBl"),
    ("Channel 2", "https://t.me/+BFnTHodoq-o2YTc9"),
    ("Channel 3", "https://t.me/+c8xbqNm8G7tmYzll"),
    ("Channel 4", "https://t.me/+SdxjhqeAvW5kMTJl"),
    ("Channel 5", "https://t.me/hyperlootzone"),
]

# /start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [[InlineKeyboardButton(name, url=link)] for name, link in CHANNELS]
    reply_markup = InlineKeyboardMarkup(keyboard)

    # reward image
    await update.message.reply_photo(
        photo="https://i.ibb.co/1mW9Wcn/congratulations.png",
        caption="🎉 *Congratulations!*\n\nAapko ek special bonus milne wala hai 🎁",
        parse_mode=ParseMode.MARKDOWN
    )

    await asyncio.sleep(2)

    text = (
        "👉 Sabhi channels join karo aur phir apna UID bhejo.\n\n"
        "⏳ Gift code aapko *jaldi hi mil jayega!* ✅"
    )

    await update.message.reply_text(
        text,
        reply_markup=reply_markup,
        parse_mode=ParseMode.MARKDOWN
    )

# UID handle
async def handle_uid(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_chat_action(chat_id=update.effective_chat.id, action=ChatAction.TYPING)
    await asyncio.sleep(3)
    await update.message.reply_text(
        "⏳ Processing...\n\n🎁 Aapka gift code *jaldi hi mil jayega* ✅",
        parse_mode=ParseMode.MARKDOWN
    )

def main():
    app = Application.builder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_uid))

    print("🤖 Bot running...")
    app.run_polling()

if __name__ == "__main__":
    main()
