from aiogram.dispatcher.filters.state import StatesGroup, State


class MessageGet(StatesGroup):
    sourcelang = State()
    endlang = State()
    message = State()
