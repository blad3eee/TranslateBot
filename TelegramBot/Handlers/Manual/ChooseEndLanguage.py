from aiogram import types, Dispatcher
from TelegramBot.States.MessageGet import MessageGet
from aiogram.dispatcher import FSMContext


class EndLangChoose:
    @staticmethod
    async def setendlang(message: types.Message, state: FSMContext):
        if message.text == 'Назад в меню':
            await state.finish()
            values_list = ['Автоопределение', 'Ввести вручную', 'Назад']
            keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
            keyboard.add(*values_list)
            await message.answer(f'Как будем переводить?', reply_markup=keyboard)
        else:
            async with state.proxy() as data:
                data['end'] = message.text
            await MessageGet.next()
            await message.answer('Введите текст, который необходимо перевести')

    @staticmethod
    def endlang_handler(dp: Dispatcher):
        dp.register_message_handler(EndLangChoose.setendlang, state=MessageGet.endlang)
