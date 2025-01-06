import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, MessageHandler, filters, ContextTypes
from datetime import datetime, timedelta
import asyncio

# Initialize logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)
logger = logging.getLogger(__name__)

# Global dictionary to store user data
user_data = {}

# Access keys for numbers 0 to 41
keys = {
     0: "B1c2D3e4F5g6H7i8",
    1: "J9k8L7m6N5o4P3q2",
    2: "R3s4T5u6V7w8X9y0",
    3: "Z7a6B5c4D3e2F1g0",
    4: "G2h3I4j5K6l7M8n9",
    5: "O1p2Q3r4S5t6U7v8",
    6: "Y3z4A5b6C7d8E9f0",
    7: "I9k8L7m0N1o2P3q4",
    8: "Q5r4S3t2U1v0W9x8",
    9: "C0d9E8f7G6h5I4j3",
    10: "U3c2B1d0F9g8H7i6",
    11: "S9e8Z7f6G5h4I3j2",
    12: "N2o3P4q5R6s7T8u9",
    13: "D8w9X0y1Z2a3B4c5",
    14: "F5u4V3w2X1y0Z9a8",
    15: "K5l6M7n8O9p0Q1r2",
    16: "W9o8N7p6Q5r4S3t2",
    17: "M3v2U1w0X9y8Z7a6",
    18: "L1m2K3n4O5p6Q7r8",
    19: "R9s8T7u6V5w4X3y2",
    20: "E0b1C2d3F4g5H6i7",
    21: "A2b3C4d5E6f7G8h9",
    22: "H1i2J3k4L5m6N7o8",
    23: "P9q8R7s6T5u4V3w2",
    24: "X0y1Z2a3B4c5D6e7",
    25: "F9g8H7i6J5k4L3m2",
    26: "T8u7V6w5X4y3Z2a1",
    27: "R5s4T3u2V1w0X9y8",
    28: "K6l5M4n3O2p1Q0r9",
    29: "E8f7G6h5I4j3K2l1",
    30: "D1e2F3g4H5i6J7k8",
    31: "M8n9O0p1Q2r3S4t5",
    32: "Z3a2B1c0D9e8F7g6",
    33: "Y5z4A3b2C1d0E9f8",
    34: "N4o5P6q7R8s9T0u1",
    35: "Q8r7S6t5U4v3W2x1",
    36: "C2d1E0f9G8h7I6j5",
    37: "V7w6X5y4Z3a2B1c0",
    38: "H3i4J5k6L7m8N9o0",
    39: "T6u5V4w3X2y1Z0a9",
    40: "B0c1D2e3F4g5H6i7",
    41: "L8m7N6o5P4q3R2s1"
}

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.message.from_user
    
    await update.message.reply_text(
        f"Hello {user.first_name}, welcome to the Tonny2.0 Bot!"
    )

    keyboard = [
        [InlineKeyboardButton("Register", url="https://tinyurl.com/48vr69at")],
        [InlineKeyboardButton("Join Channel", url="https://t.me/TeamEarningZone")],
        [InlineKeyboardButton("Check Join", callback_data="check_join")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    warning_message = (
        "⚠️ *Important Notice:*\n\n"
        "To create a successful account, please click the *'Register'* button. "
        "Using this mod on an existing account will render the mod non-functional. "
        "Please ensure to register a new account to enjoy all features seamlessly.\n\n"
        
            "⚠️ *महत्वपूर्ण सूचना:*\n\n"
        "एक सफल खाता बनाने के लिए कृपया *'Register'* बटन पर क्लिक करें। "
        "इस मॉड का उपयोग एक मौजूदा खाते पर करने से मॉड कार्यशील नहीं होगा। "
        "कृपया सभी सुविधाओं का लाभ उठाने के लिए एक नया खाता पंजीकृत करें।"
    )

    await update.message.reply_text(warning_message, parse_mode='Markdown')
    await update.message.reply_text("Join & Register ⬇️", reply_markup=reply_markup)

async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    user_id = query.from_user.id

    if query.data == "check_join":
        if user_id in user_data and user_data[user_id].get("joined", False):
            await query.answer("You have already joined the channel!")
            await query.message.reply_text("Thanks for Joining Us 😉")
            await ask_get_key_button(query, context)
        else:
            user_data[user_id] = {"joined": True}
            await query.answer("Channel join verified!")
            await query.message.reply_text("You have joined the channel! You can now proceed to get your access key.")
            await ask_get_key_button(query, context)

async def ask_get_key_button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("Get Key 🔐", callback_data="get_key")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("Click the button to get your access key 🗝️", reply_markup=reply_markup)

async def get_key_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    notice_message = (
        "ℹ️ *Important Reminder:*\n\n"
        "Before using this mode, please ensure you register using our provided link. "
        "Recharge a minimum of ₹500 or ₹1000 to enhance your chances of winning significantly. "
        "Your success is our priority!\n\n"
        
         "ℹ️ *महत्वपूर्ण अनुस्मारक:*\n\n"
        "इस मोड का उपयोग करने से पहले, कृपया सुनिश्चित करें कि आप हमारे दिए गए लिंक का उपयोग करके *'Register'* करें। "
        "अपनी जीतने की संभावनाओं को बढ़ाने के लिए न्यूनतम ₹500 या ₹1000 का रिचार्ज करें। "
        "आपकी सफलता हमारी प्राथमिकता है!"
    )
    await query.message.reply_text(notice_message, parse_mode='Markdown')
    await query.message.reply_text("Enter your access number 👇 :")

async def handle_access_number(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.message.from_user
    user_id = user.id
    message_text = update.message.text

    if user_id in user_data and "last_access_time" in user_data[user_id]:
        last_access_time = user_data[user_id]["last_access_time"]
        if datetime.now() - last_access_time < timedelta(hours=24):
            remaining_time = timedelta(hours=24) - (datetime.now() - last_access_time)
            await update.message.reply_text(f"😔 Sorry, you can only request a key once every 24 hours. "
                                            f"Please try again in {remaining_time}.")
            return

    try:
        access_number = int(message_text)
        if access_number in keys:
            access_key = keys[access_number]
            await update.message.reply_text(f"{user.first_name}, Your access key 🗝️ : {access_key}")
            user_data[user_id]["last_access_time"] = datetime.now()
        else:
            await update.message.reply_text("Invalid access number. Please enter a number between 0 and 41.")
    except ValueError:
        await update.message.reply_text("Please enter a valid number between 0 and 41.")

async def background_worker():
    while True:
        await asyncio.sleep(60)

def main():
    application = Application.builder().token("7279695237:AAHn4JeJcWmW0yc2dOUCmPr1fbgpYKenmco").build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CallbackQueryHandler(button_handler, pattern="check_join"))
    application.add_handler(CallbackQueryHandler(get_key_handler, pattern="get_key"))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_access_number))

    # Start the bot
    application.run_polling()

if __name__ == "__main__":
    main()
