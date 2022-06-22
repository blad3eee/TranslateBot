from aiogram import types, Dispatcher
from TelegramBot.States.MessageGet import MessageGet
from aiogram.dispatcher import FSMContext


class LangChoose:
    """Выбор искомого языка"""
    @staticmethod
    async def setlang(message: types.Message, state: FSMContext):
        if message.text == 'Назад в меню':
            await state.finish()
            values_list = ['Автоопределение', 'Ввести вручную', 'Назад']
            keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
            keyboard.add(*values_list)
            await message.answer(f'Как будем переводить?', reply_markup=keyboard)
        else:
            async with state.proxy() as data:
                data['source'] = message.text
            await MessageGet.next()
            await message.answer('Введите язык, на который необходимо перевести текст')

    @staticmethod
    def setlang_handler(dp: Dispatcher):
        dp.register_message_handler(LangChoose.setlang, state=MessageGet.sourcelang)
