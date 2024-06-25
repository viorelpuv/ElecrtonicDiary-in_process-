from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder, InlineKeyboardButton


class UsersKeyboard:
    def __init__(self):
        self.reply_kb = ReplyKeyboardMarkup
        self.inline_kb = InlineKeyboardBuilder

    def StartNotRegisterUser(self):
        return self.reply_kb(keyboard=[[
            KeyboardButton(text="Регистрация")
        ]], resize_keyboard=True, one_time_keyboard=True)

    def NewUserWebLink(self):
        kb = self.inline_kb().add(InlineKeyboardButton(
            text="Дневник",
            url="https://google.com",
            callback_data="new_user_web_link"
        ))
        kb.adjust(1)
        return kb.as_markup()

    def StartRegisterUser(self):
        return self.reply_kb(keyboard=[[
            KeyboardButton(text='Личный кабинет')
        ]], resize_keyboard=True, one_time_keyboard=True)
