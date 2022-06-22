from aiogram import types, Dispatcher
from aiogram.dispatcher.filters import Text


class BackToTranslateChoose:
    """Обработчик команды 'Назад в меню'"""
    @staticmethod
    async def back_to_choose(message: types.Message):
        values_list = ['Автоопределение', 'Ввести вручную', 'Назад']
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.add(*values_list)
        await message.answer(f'Как будем переводить?', reply_markup=keyboard)

    @staticmethod
    def backto_handler(dp: Dispatcher):
        dp.register_message_handler(BackToTranslateChoose.back_to_choose, Text(equals='Назад в меню'))
