import logging

from telegram.ext import Updater, CommandHandler, MessageHandler, RegexHandler, Filters

from handlers import *
import settings

logging.basicConfig(format='%(asctime)s-%(levelname)s-%(message)s',
                    level=logging.INFO,
                    filename='bot.log'
                    )


def main():
    mybot = Updater(settings.API_KEY, use_context=True)
    
    logging.info('Бот запускается')

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler('start', greet_user, pass_user_data=True))
    dp.add_handler(CommandHandler('cat', send_cat_pictures, pass_user_data=True))
    dp.add_handler(MessageHandler(Filters.regex(r'Прислать котика'), 
                                  send_cat_pictures, pass_user_data=True))
    dp.add_handler(MessageHandler(Filters.regex(r'Сменить аватарку'), 
                                  change_avatar, pass_user_data=True))
    dp.add_handler(MessageHandler(Filters.contact, get_contact, pass_user_data=True))
    dp.add_handler(MessageHandler(Filters.location, get_location, pass_user_data=True))
  
    dp.add_handler(MessageHandler(Filters.text, talk_to_me, pass_user_data=True))

    mybot.start_polling()
    mybot.idle
    

main()


