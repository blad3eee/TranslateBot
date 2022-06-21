from aiogram import types, Dispatcher
from aiogram.dispatcher.filters import Text
from TelegramBot.States.MessageGet import MessageGet


class TranslateText:
    @staticmethod
    async def translate(message: types.Message):
        values_list = ['Назад в меню']
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.add(*values_list)
        await MessageGet.sourcelang.set()
        await message.answer('Введите искомый язык', reply_markup=keyboard)

    @staticmethod
    def translate_handler(dp: Dispatcher):
        dp.register_message_handler(TranslateText.translate, Text(equals='Ввести вручную'))
