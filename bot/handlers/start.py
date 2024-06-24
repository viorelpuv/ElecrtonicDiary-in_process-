import os

from aiogram import Bot
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from bot.utils.database import Database
from bot.keyboards.usersKeyboard import UsersKeyboard
from bot.states.stateRegistration import Registration


# !!! НАДО ДОБАВИТЬ ЛОГИН !!! #

async def start(msg: Message, bot: Bot):
    user = msg.from_user.id
    username = msg.from_user.username
    db = Database()
    kb = UsersKeyboard()
    all_users = db.select_users(user_id=user)
    if all_users:
        await bot.send_message(user, "Добро пожаловать!", reply_markup=kb.StartRegisterUser())
    else:
        await bot.send_message(user, f"👋🏼 Привет, {username}!\nРад видеть тебя здесь. Функционала пока нет, "
                                        f"но ты зарегайся :)", reply_markup=kb.StartNotRegisterUser())


async def startRegistrationFio(msg: Message, bot: Bot, state: FSMContext):
    user = msg.from_user.id
    await bot.send_message(user, "Как ваз зовут? Напишите свое ФИО (Например: Иванов Иван Иванович)")
    await state.set_state(Registration.fio)


async def startRegistrationGroup(msg: Message, bot: Bot, state: FSMContext):
    user = msg.from_user.id
    if len(msg.text.split()) == 3:
        await state.update_data(fio=msg.text.split())
        await bot.send_message(user, "Отлично! В какой группе ты учишься? (Например: ЛС-31)")
        await state.set_state(Registration.group)
    else:
        await bot.send_message(user, "Что-то пошло не так. Ты правильно ввел свое ФИО? Введи еще раз!")
        return


async def startRegistrationPassword(msg: Message, bot: Bot, state: FSMContext):
    user = msg.from_user.id
    await state.update_data(group=msg.text)
    await bot.send_message(user, "Теперь придумай пароль для личного кабинета")
    await state.set_state(Registration.password)


async def startRegistrationFinish(msg: Message, bot: Bot, state: FSMContext):
    user = msg.from_user.id
    db = Database()
    kb = UsersKeyboard()
    await state.update_data(password=msg.text)
    data = await state.get_data()

    db.add_user(
        user_id=user,
        second_name=data['fio'][0],
        first_name=data['fio'][1],
        middle_name=data['fio'][2],
        group=data['group'],
        password=data['password']
    )

    await bot.send_message(user, f"Успешно! Теперь вы можете войти в личный кабинет на нашем сайте 😊",
                           reply_markup=kb.NewUserWebLink())
