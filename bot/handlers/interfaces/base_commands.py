from typing import Protocol

from aiogram import Dispatcher


class BaseHandler(Protocol):
    def __call__(self, dp: Dispatcher) -> None:
        """
        отвечает за добавление обработчиков
        для действий(callback query, messages, commands)
        или обработка конкретного стейта
        """
        ...