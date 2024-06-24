from aiogram.fsm.state import State, StatesGroup


# !!! НАДО ДОБАВИТЬ ЛОГИН !!! #
class Registration(StatesGroup):
    fio = State()
    group = State()
    password = State()
