# Telegram Bot in Python

Let's spin up a simple working example. More details [here](https://github.com/python-telegram-bot/python-telegram-bot). Then the world is your oyster.

1. Install python-telegram-bot with `pip install python-telegram-bot --upgrade`
2. Create a new file called `bot.py`.
3. Paste into `bot.py` the following code:

```{python}
import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler, filters

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Welcome to ULTA 2024. Remember two of our core principles?\n\nAsk with /principles")

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Sorry, I didn't get that.")

async def principles(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="1. Learn Together.\n2. Prefer People to Phones.\n\nLet's have a great ULTA 2024 together!")

if __name__ == '__main__':
    application = ApplicationBuilder().token('7284308646:AAFRIZYlNT03hJEfpCuE3RY5m4AoW9ZjFTA').build()
    
    start_handler = CommandHandler('start', start)
    application.add_handler(start_handler)

    echo_handler = MessageHandler(filters.TEXT & (~filters.COMMAND), echo)
    application.add_handler(echo_handler)

    principles_handler = CommandHandler('principles', principles)
    application.add_handler(principles_handler)
    
    application.run_polling()
``` 

4. Run `python bot.py`.
5. Check out the example bot we built at [t.me/ulta2024\_test\_bot](t.me/ulta2024_test_bot). Try `/start` and `/principles`.

The bot is extensible by changing to handlers and response functions. Time to implement the ideas in your imagination!
