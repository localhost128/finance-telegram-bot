import logging
from datetime import datetime, timedelta

from telegram import Update
from telegram.ext import (
    filters,
    ApplicationBuilder,
    ContextTypes,
    CommandHandler,
)

import config
import message_texts
import items


logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)


async def start(_: Update, context: ContextTypes.DEFAULT_TYPE):
    await _send_message(context, message_texts.START_HELP)


async def confirm(_: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        items.confirm()
        await _send_message(context, message_texts.CONFIRM_SUCCESS)
    except Exception:
        await _send_message(context, message_texts.ERROR)


async def cancel(_: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        items.cancel()
        await _send_message(context, message_texts.CANCEL_SUCCESS)
    except Exception:
        await _send_message(context, message_texts.ERROR)


async def add_item(_: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        item = _parse_args(context.args)
        if not item.category:
            item.category = items.predict_category(item.name)
        items.add_item(item)
        await _send_message(
            context,
            text=message_texts.ITEM.format(
                name=item.name,
                cost=item.cost / 100,
                category=item.category,
                date=item.date,
            ),
        )

    except Exception as e:
        await _send_message(context, text=f"Error: {e}")


def _parse_args(args: list[str] | None) -> items.Item:
    match args:
        case cost, name:
            return items.Item(
                name=name,
                cost=_pasrse_cost(cost),
            )

        case cost, name, category:
            return items.Item(
                name=name,
                cost=_pasrse_cost(cost),
                category=_parse_category(category),
            )

        case cost, name, category, date:
            return items.Item(
                name=name,
                cost=_pasrse_cost(cost),
                category=_parse_category(category),
                date=datetime.now() + timedelta(days=int(date)),
            )

        case _:
            raise Exception(message_texts.WRONG_PARAMETERS_NUMBER_ERROR)


def _pasrse_cost(text: str) -> int:
    text = text.replace(",", ".")
    try:
        return int(text) * 100
    except ValueError:
        pass

    try:
        return int(f"{float(text):.2f}".replace(".", ""))
    except ValueError:
        raise Exception(message_texts.WRONG_COST_ERROR)


def _parse_category(text: str) -> str | None:
    if text == "0":
        return None

    if text.isdigit() and (category_id := int(text)) <= len(items.CATEGORIES):
        return items.CATEGORIES[category_id - 1]

    if text in items.CATEGORIES:
        return text

    raise Exception(message_texts.WRONG_CAREGORY_ERROR)


async def _send_message(context: ContextTypes.DEFAULT_TYPE, text: str):
    await context.bot.send_message(chat_id=config.MY_CHAT_ID, text=text)


if __name__ == "__main__":
    application = ApplicationBuilder().token(config.TELEGRAM_BOT_TOKEN).build()

    command_callbacks = {
        "start": start,
        "help": start,
        "add": add_item,
        "confirm": confirm,
        "cancel": cancel,
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
