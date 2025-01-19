from typing import Protocol


class SomeClientProtocol(Protocol):
    def get_some_info(self):
        ...