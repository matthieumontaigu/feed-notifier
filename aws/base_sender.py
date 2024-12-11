from abc import ABC, abstractmethod


class BaseSender(ABC):

    @abstractmethod
    def send(self, source: str, destination: str, subject: str, message: str) -> None:
        """Send a message from source to the destination."""
        pass
