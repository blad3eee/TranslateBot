from aiogram import types, Dispatcher


class HelpComma:
    @staticmethod
    async def help(message: types.Message):
        await message.answer(f'Я бот-переводчик\n'
                             f'Введите команду /start чтобы начать работу со мной\n'
                             f'Перевод - переведу ваше слово с практически любого языка на любой другой\n'
                             f'Случайное слово - выведу случайное слово на русском языке и его перевод на нескольких '
                             f'языках.')

    @staticmethod
    def help_handler(dp: Dispatcher):
        dp.register_message_handler(HelpComma.help, commands='help')
