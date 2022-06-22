from aiogram import types, Dispatcher
from TelegramBot.States.AutoMessageGet import AutoMessageGet
from aiogram.dispatcher import FSMContext


class AutoEndLangChoose:
    """Выбор языка перевода"""
    @staticmethod
    async def autosetendlang(message: types.Message, state: FSMContext):
        if message.text == 'Назад в меню':
            await state.finish()
            values_list = ['Автоопределение', 'Ввести вручную', 'Назад']
            keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
            keyboard.add(*values_list)
            await message.answer(f'Как будем переводить?', reply_markup=keyboard)
        else:
            async with state.proxy() as data:
                data['end'] = message.text
            await AutoMessageGet.next()
            await message.answer('Введите текст, который необходимо перевести')

    @staticmethod
    def autoendlang_handler(dp: Dispatcher):
        dp.register_message_handler(AutoEndLangChoose.autosetendlang, state=AutoMessageGet.endlang)
