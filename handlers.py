from glob import glob
from random import choice

from utils import get_keyboard, greet_user_emo


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
