from telegram.ext import Updater, MessageHandler, Filters
from telegram.ext import CommandHandler
from Wiki import search_wiki

TOKEN = "5538204452:AAFX8CEIaueT3XY_edY4d6I91hLRib1JvYY"


def echo(update, context):
    txt = update.message.text
    if txt.lower() in ["привет", "здаров"]:
        txt = "И тебе привет!"
    update.message.reply_text(txt)


def start(update, context):
    update.message.reply_text("Бот запущен!")

def wiki(update, context):
        print(context.args)
        word = "".join(context.args)
        if word:
            update.message.reply_text("Идет поиск...")
            summary, url = search_wiki(word)
            update.message.reply_text(summary+url)
        else:
            update.message.reply_text("Необходимо ввести что искать")


def main():
    updater = Updater(TOKEN, use_context = True)
    dp = updater.dispatcher
    print("Бот запущен")

    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(CommandHandler('wiki', wiki))
    dp.add_handler(MessageHandler(Filters.text, echo))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
