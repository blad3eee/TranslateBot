from aiogram.dispatcher.filters.state import StatesGroup, State


class MessageGet(StatesGroup):
    """Состояния для ручного ввода искомого языка"""
    sourcelang = State()
    endlang = State()
    message = State()
