import httpx
from typing import Mapping

from bot.handlers.interfaces.clients.some_client import SomeClientProtocol


class SomeClientImpl(SomeClientProtocol):
    def __init__(self, some_url: str) -> None:
        self.__some_url = some_url

    async def _request(
        self,
        method: str,
        extra_path: str,
        *,
        query_params: Mapping[str, str] | None = None,
        json_body: Mapping[str, str] | None = None,
    ) -> httpx.Response:
        url = httpx.URL(self.__some_url).join(extra_path)

        async with httpx.AsyncClient() as client:
            response = await client.request(
                method,
                url=str(url),
                params=query_params,
                json=json_body,
            )

        return response

    def get_some_info(self):
        """обработка нужных статус кодов, приводим к нужной модели"""
        pass
