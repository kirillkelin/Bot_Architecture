from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

"""Пример инлайн клавиатуры, которая может возвращаться пользователю"""

def back_keyboard() -> InlineKeyboardMarkup:
    """ Клавиатура возвращения """
    back = InlineKeyboardButton(text='Назад', callback_data='back')
    keyboard = InlineKeyboardMarkup()
    keyboard.add(back)
    return keyboard