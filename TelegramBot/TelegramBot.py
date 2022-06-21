from aiogram.utils import executor

from .BotConfig.BotSetup import BotSetup
from .Handlers import *


class TelegramBot:

    StartBot.start_handler(BotSetup.dp)
    HelpComma.help_handler(BotSetup.dp)
    ChooseMethod.choose_handler(BotSetup.dp)
    RandomTranslate.random_handler(BotSetup.dp)
    AutoTranslateText.autotranslate_handler(BotSetup.dp)
    AutoEndLangChoose.autoendlang_handler(BotSetup.dp)
    AutoSetText.autotext_handler(BotSetup.dp)
    TranslateText.translate_handler(BotSetup.dp)
    LangChoose.setlang_handler(BotSetup.dp)
    EndLangChoose.endlang_handler(BotSetup.dp)
    SetText.text_handler(BotSetup.dp)
    BackToTranslateChoose.backto_handler(BotSetup.dp)
    BackToMenu.back_handler(BotSetup.dp)

    executor.start_polling(BotSetup.dp, skip_updates=True)
