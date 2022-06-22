from aiogram import types, Dispatcher
from aiogram.dispatcher.filters import Text


class BackToMenu:
    """Обработчик команды 'Назад'"""
    @staticmethod
    async def back_to_menu(message: types.Message):
        values_list = ['Перевод', 'Случайное слово']
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.add(*values_list)
        await message.answer(f'Выберите функцию', reply_markup=keyboard)

    @staticmethod
    def back_handler(dp: Dispatcher):
        dp.register_message_handler(BackToMenu.back_to_menu, Text(equals='Назад'))
