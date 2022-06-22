from aiogram import types, Dispatcher
from aiogram.dispatcher.filters import Text
import random
from Data.words import words_list
import aiohttp


class RandomTranslate:
    """Обработчик команды 'Случайное слово'"""
    @staticmethod
    async def random_word(message: types.Message):
        values_list = ['Перевод', 'Случайное слово']
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.add(*values_list)
        word = random.choice(words_list)
        params_en = {'engine': 'google', 'to': 'en', 'text': word}
        params_fr = {'engine': 'google', 'to': 'fr', 'text': word}
        params_es = {'engine': 'google', 'to': 'es', 'text': word}

        await message.answer('На русском: '+str(word))

        async with aiohttp.ClientSession() as session:
            async with session.get(url='https://simplytranslate.org/api/translate/', params=params_en) as resp:
                response = await resp.json()
                await message.answer('На английском: '+str(response['translated-text']), reply_markup=keyboard)

        async with aiohttp.ClientSession() as session:
            async with session.get(url='https://simplytranslate.org/api/translate/', params=params_fr) as resp:
                response = await resp.json()
                await message.answer('На французском: '+str(response['translated-text']), reply_markup=keyboard)

        async with aiohttp.ClientSession() as session:
            async with session.get(url='https://simplytranslate.org/api/translate/', params=params_es) as resp:
                response = await resp.json()
                await message.answer('На испанском: '+str(response['translated-text']), reply_markup=keyboard)

    @staticmethod
    def random_handler(dp: Dispatcher):
        dp.register_message_handler(RandomTranslate.random_word, Text(equals='Случайное слово'))
