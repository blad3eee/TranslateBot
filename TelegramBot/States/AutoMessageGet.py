from aiogram.dispatcher.filters.state import StatesGroup, State


class AutoMessageGet(StatesGroup):
    """Состояния для Автоопределения языка ввода"""
    endlang = State()
    message = State()
