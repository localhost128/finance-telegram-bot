import logging
from telegram import Update
from telegram.ext import (
    filters,
    ApplicationBuilder,
    ContextTypes,
    CommandHandler,
)

import config
import message_texts


logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)


async def start(_: Update, context: ContextTypes.DEFAULT_TYPE):
    await _send_message(context, message_texts.START_HELP)


async def _send_message(context: ContextTypes.DEFAULT_TYPE, text: str):
    await context.bot.send_message(chat_id=config.MY_CHAT_ID, text=text)


if __name__ == "__main__":
    application = ApplicationBuilder().token(config.TELEGRAM_BOT_TOKEN).build()

    command_callbacks = {
        "start": start,
        "help": start,
    }

    for command, callback in command_callbacks.items():
        application.add_handler(
            CommandHandler(
                command=command,
                callback=callback,
                filters=filters.Chat(chat_id=config.MY_CHAT_ID),
            )
        )

    application.run_polling()
