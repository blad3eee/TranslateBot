from aiogram import types, Dispatcher
from aiogram.dispatcher.filters import Text


class ChooseMethod:
    """Обработчик команды 'Перевод'"""
    @staticmethod
    async def choose_translate_method(message: types.Message):
        values_list = ['Автоопределение', 'Ввести вручную', 'Назад']
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.add(*values_list)
        await message.answer(f'Как будем переводить?', reply_markup=keyboard)

    @staticmethod
    def choose_handler(dp: Dispatcher):
        dp.register_message_handler(ChooseMethod.choose_translate_method, Text(equals='Перевод'))
