from aiogram import types, Bot, Dispatcher

from TelegramBot.BotConfig import config
from aiogram.contrib.fsm_storage.memory import MemoryStorage


class BotSetup:
    bot = Bot(token=config.BOT_TOKEN, parse_mode=types.ParseMode.HTML)
    storage = MemoryStorage()
    dp = Dispatcher(bot, storage=storage)
