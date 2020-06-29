# -*- coding: utf-8 -*-
from glob import glob
import logging
from random import choice

from emoji import emojize
from telegram import ReplyKeyboardMarkup,KeyboardButton
from telegram.ext import Updater, CommandHandler, MessageHandler, RegexHandler, Filters

import settings

logging.basicConfig(format='%(asctime)s-%(levelname)s-%(message)s',
                    level=logging.INFO,
                    filename='bot.log'
                    )

def greet_user(update, context):
    user_data=context.user_data
    emo = greet_user_emo(user_data)
    user_data['emo']=emo
    text='Привет {}'.format(emo)
    update.message.reply_text(text, reply_markup=get_keyboard())

def talk_to_me(update, context):
    user_data=context.user_data
    data=[update.message.chat.first_name, user_data['emo'], update.message.text]
    user_text = f"Привет {data[0]} {data[1]}! Ты написал: {data[2]}"
    logging.info("User: %s, Chat id: %s, Message: %s", update.message.chat.username, 
                 update.message.chat.id, update.message.text)
    update.message.reply_text(user_text, reply_markup=get_keyboard())

def send_cat_pictures(update, context):
    cat_list = glob('images/*.jpg')
    cat_pic = choice(cat_list)
    bot=context.bot
    bot.send_photo(chat_id=update.message.chat.id, photo=open(cat_pic, 'rb'), reply_markup=get_keyboard())

def change_avatar(update, context):
    user_data=context.user_data
    if 'emo' in user_data:
        del user_data['emo']
    emo = greet_user_emo(user_data)
    update.message.reply_text('Готово: {}'.format(emo), reply_markup=get_keyboard())

def get_contact(update, context):
    user_data=context.user_data
    print(update.message.contact)
    update.message.reply_text('Готово: {}'.format(greet_user_emo(user_data)), reply_markup=get_keyboard())

def get_location(update, context):
    user_data=context.user_data
    print(update.message.location)
    update.message.reply_text('Готово: {}'.format(greet_user_emo(user_data)), reply_markup=get_keyboard())

def greet_user_emo(user_data):
    if 'emo' in user_data:
        return user_data['emo']
    else:
        user_data['emo'] = emojize(choice(settings.USER_EMOJI), use_aliases=True)
        return user_data['emo']
def get_keyboard():
    contact_button = KeyboardButton('Прислать контакты', request_contact=True)
    location_button = KeyboardButton('Прислать координаты', request_location=True)
    my_keyboard = ReplyKeyboardMarkup([
                                        ['Прислать котика', 'Сменить аватарку'],
                                        [contact_button, location_button]
                                       ], resize_keyboard=True
                                      )
    return my_keyboard


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


