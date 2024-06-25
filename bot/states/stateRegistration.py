from aiogram.fsm.state import State, StatesGroup


class Registration(StatesGroup):
    fio = State()
    group = State()
    password = State()
