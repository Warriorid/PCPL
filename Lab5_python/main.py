from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes
TOKEN = "7930822410:AAEjYc4I51T2jL7xE_kKcQATpmTh8Xxf9nQ"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    keyboard = [
        [InlineKeyboardButton("Кнопка 1", callback_data='1')],
        [InlineKeyboardButton("Кнопка 2", callback_data='2')],
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text('Выберите опцию:', reply_markup=reply_markup)


async def button(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    await query.answer()
    await query.edit_message_text(text=f"Вы выбрали опцию {query.data}")


def main() -> None:
    application = Application.builder().token(TOKEN).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CallbackQueryHandler(button))

    application.run_polling()

if __name__ == '__main__':
    main()

