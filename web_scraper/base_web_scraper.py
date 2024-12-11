from abc import ABC, abstractmethod

from schema.item import Item


class BaseWebScraper(ABC):

    def __init__(self, url: str) -> None:
        self.url = url

    @abstractmethod
    def get(self) -> list[Item]:
        """Retrieve content of the url and parse it"""
        pass
