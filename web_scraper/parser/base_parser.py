from abc import ABC, abstractmethod

from schema.item import Item


class BaseParser(ABC):

    def __init__(self, url: str) -> None:
        self.url = url

    @abstractmethod
    def parse(self, html) -> list[Item]:
        """Parse HTML into a list of items"""
        pass
