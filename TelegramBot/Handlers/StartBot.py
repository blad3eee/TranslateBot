from aiogram import types, Dispatcher


class StartBot:
    """Обработчик команды /start"""
    @staticmethod
    async def start(message: types.Message):
        values_list = ['Перевод', 'Случайное слово']
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.add(*values_list)
        await message.answer(f'Выберите функцию', reply_markup=keyboard)

    @staticmethod
    def start_handler(dp: Dispatcher):
        dp.register_message_handler(StartBot.start, commands='start')
