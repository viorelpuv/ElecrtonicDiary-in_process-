from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder


class UsersKeyboard:
    def __init__(self):
        self.reply_kb = ReplyKeyboardMarkup
        self.inline_kb = InlineKeyboardBuilder

    def StartNotRegisterUser(self):
        return self.reply_kb(keyboard=[[
            KeyboardButton(text="Регистрация")
        ]], resize_keyboard=True, one_time_keyboard=True)

    def StartRegisterUser(self):
        pass
