from aiogram import Dispatcher

from bot.handlers.interfaces.base_commands import BaseHandler
from bot.handlers.interfaces.clients.some_client import SomeClientProtocol


class SomeHandlerImpl(BaseHandler):
    def __init__(self, some_client: SomeClientProtocol) -> None:
        self.__some_client = some_client

    def __call__(self, dp: Dispatcher) -> None:
        """
        Пример реализации:
        dp.message.register(self.set_email, state=Auth.email)
        Обработка ввода пользователем какого-то email - это соответсвует стейту Auth.email,
        на него будет реагировать обработчик set_email, логика которого должна быть описана в этом классе
        """
        pass
