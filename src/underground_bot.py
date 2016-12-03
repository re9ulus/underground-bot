from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


def start(bot, update):
    update.message.reply_text('Hi!')


def start(bot, update):
    print('request: start')
    bot.sendMessage(chat_id=update.message.chat_id,
                    text='I\'m a bot, please talk to me !')


def echo(bot, update):
    print('request: echo')
    bot.sendMessage(chat_id=update.message.chat_id,
                    text=update.message.text.replace(' ', '_'))


def caps(bot, update, args):
    print('request: cups')
    text_caps = ' '.join(args).upper()
    bot.sendMessage(chat_id=update.message.chat_id,
                    text=text_caps)


def error(bot, update,error):
    logger.warn('Update "%s" caused error "%s"' % (update, error))

def main():
    updater = Updater(token='')
    dispatcher = updater.dispatcher

    start_handler = CommandHandler('start', start)
    dispatcher.add_handler(start_handler)

    echo_handler = MessageHandler(Filters.text, echo)
    dispatcher.add_handler(echo_handler)

    caps_handler = CommandHandler('caps', caps, pass_args=True)
    dispatcher.add_handler(caps_handler)

    dispatcher.add_error_handler(error)

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
