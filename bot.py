from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

# 🔑 अपना BotFather वाला Token यहां डालो
TOKEN = "7709087276:AAE4Gh04ucQWDkANg0UCbK6p3qLb8mUhquM"

# ✅ जिन channels को join करवाना है (links डालो)
CHANNELS = [
    "https://t.me/+uSy_l51dEitiMGU1",
    "https://t.me/+BFnTHodoq-o2YTc9",
    "https://t.me/+c8xbqNm8G7tmYzll",
    "https://t.me/+SdxjhqeAvW5kMTJl"
]

# 🔹 Start Command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [[InlineKeyboardButton("✅ Join Channels", callback_data="check")]]
    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(
        "👋 Welcome to Free Paytm Cash Bot!\n\n"
        "👉 पहले इन channels को join करो, तभी आगे बढ़ पाओगे 👇\n\n" +
        "\n".join(CHANNELS),
        reply_markup=reply_markup
    )

# 🔹 Channel Check (Fake Verification)
async def check_channels(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    # ⚠️ यहां असली verification नहीं है, सिर्फ दिखाने के लिए fake check
    keyboard = [[InlineKeyboardButton("💰 Claim Free Paytm Cash", callback_data="payment")]]
    reply_markup = InlineKeyboardMarkup(keyboard)

    await query.edit_message_text(
        "✅ Channels join हो गए!\n\nअब अपना reward लो 👇",
        reply_markup=reply_markup
    )

# 🔹 Fake Payment Page
async def payment_page(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    await query.edit_message_text(
        "💸 आपने 50₹ Paytm Cash Claim किया है!\n\n"
        "🕒 Payment Process हो रहा है...\n\n"
        "⚠️ Note: यह demo है, असली पैसे नहीं मिलेंगे!"
    )

# 🔹 Main Function
def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(check_channels, pattern="check"))
    app.add_handler(CallbackQueryHandler(payment_page, pattern="payment"))

    print("🤖 Bot is running...")
    app.run_polling()
if _name_ == "_main_":
    main()
