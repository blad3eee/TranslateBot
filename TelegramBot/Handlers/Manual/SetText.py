from aiogram import types, Dispatcher
from TelegramBot.States.MessageGet import MessageGet
from aiogram.dispatcher import FSMContext
from Data.languages import sourceLanguagesDict, endLanguagesDict
import aiohttp


class SetText:
    @staticmethod
    async def settext(message: types.Message, state: FSMContext):
        if message.text == 'Назад в меню':
            await state.finish()
            values_list = ['Автоопределение', 'Ввести вручную', 'Назад']
            keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
            keyboard.add(*values_list)
            await message.answer(f'Как будем переводить?', reply_markup=keyboard)
        else:
            async with state.proxy() as data:
                data['text'] = message.text

            async with state.proxy() as data:
                values_list = ['Перевод', 'Случайное слово']
                keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
                keyboard.add(*values_list)

                params = {'engine': 'google', 'from': sourceLanguagesDict[data['source'].lower()],
                          'to': endLanguagesDict[data['end'].lower()], 'text': data['text']}
                async with aiohttp.ClientSession() as session:
                    async with session.get(url='https://simplytranslate.org/api/translate/', params=params) as resp:
                        response = await resp.json()
                        await message.answer(response['translated-text'], reply_markup=keyboard)
            await state.finish()

    @staticmethod
    def text_handler(dp: Dispatcher):
        dp.register_message_handler(SetText.settext, state=MessageGet.message)
