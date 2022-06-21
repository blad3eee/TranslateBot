from aiogram.dispatcher.filters.state import StatesGroup, State


class AutoMessageGet(StatesGroup):
    endlang = State()
    message = State()
