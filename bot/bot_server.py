import asyncio

from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from dishka.integrations.aiogram import setup_dishka
from loguru import logger

from bot.handlers.commands.some_entity_commands import SomeHandlerImpl
from bot.requests.some_client import SomeClientImpl
from config import get_config

config = get_config()

class BotServer:
    def __init__(self):
        self.__bot: Bot | None = None
        self.__dp: Dispatcher | None = None

        self.initialized: bool = False

    def __on_start_up(self):
        logger.info('startup bot')

    def __on_shutdown(self):
        logger.info('shutdown bot')

    # def __setup_containers(self):
    #     setup_dishka(container=container, router=self.__dp, auto_inject=True)

    def setup(self):
        self.__dp = Dispatcher(storage=MemoryStorage())  # можно прикрутить редис
        self.__bot = Bot(token=config.BOT_TOKEN)

        client = SomeClientImpl(some_url=config.SOME_URL)
        SomeHandlerImpl(some_client=client)(self.__dp)

        self.initialized = True

        self.__dp.startup.register(self.__on_start_up)
        self.__dp.shutdown.register(self.__on_shutdown)

    def run_polling(self) -> None:
        asyncio.run(self.__dp.start_polling(self.__bot))