from aiogram import types, Dispatcher
from aiogram.dispatcher.filters import Text
from TelegramBot.States.AutoMessageGet import AutoMessageGet


class AutoTranslateText:
    @staticmethod
    async def autotranslate(message: types.Message):
        values_list = ['Назад в меню']
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.add(*values_list)
        await AutoMessageGet.endlang.set()
        await message.answer('Введите язык, на который необходимо перевести текст', reply_markup=keyboard)

    @staticmethod
    def autotranslate_handler(dp: Dispatcher):
        dp.register_message_handler(AutoTranslateText.autotranslate, Text(equals='Автоопределение'))
