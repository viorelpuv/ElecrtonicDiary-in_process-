import os
import asyncio
import logging
from dotenv import load_dotenv

from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command
from aiogram.fsm.storage.memory import MemoryStorage

from bot.handlers.start import (start, startRegistrationFio, startRegistrationGroup, startRegistrationPassword,
                                startRegistrationFinish)
from bot.states.stateRegistration import Registration

load_dotenv()
logging.basicConfig(level=logging.INFO)

token = os.getenv('token')
admin = os.getenv('admin')

bot = Bot(token=token)
dp = Dispatcher(storage=MemoryStorage())


# #~#~#~# [ Сообщение при запуске бота ] #~#~#~#
async def startBot():
    await bot.send_message(admin, "Start Bot")


# #~#~#~# [ Инициализация сообщения при запуске бота ] #~#~#~#
dp.startup.register(startBot)

# #~#~#~# [ Хендлеры на старт ] #~#~#~#
dp.message.register(start, Command('start'))


# !!! НАДО ДОБАВИТЬ ЛОГИН !!! #
dp.message.register(startRegistrationFio, F.text == "Регистрация")
dp.message.register(startRegistrationGroup, Registration.fio)
dp.message.register(startRegistrationPassword, Registration.group)
dp.message.register(startRegistrationFinish, Registration.password)


async def main():
    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()


if __name__ == '__main__':
    asyncio.run(main())
