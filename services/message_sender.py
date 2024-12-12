from aws.sender_factory import get_sender
from schema.item import Item


class MessageSender(object):

    def __init__(
        self,
        message_type: str,
        aws_credentials: dict[str, str],
        sources: dict[str, str],
        destination: str,
    ) -> None:
        self.sender = get_sender(message_type, aws_credentials)
        self.sources = sources
        self.destination = destination

    def send_message(self, subject: str, message: str) -> None:
        self.sender.send(
            source=self.get_default_source(),
            destination=self.destination,
            subject=subject,
            message=message,
        )

    def send_items(self, items: list[Item]) -> None:
        for item in items:
            self.send_item(item)

    def send_item(self, item: Item) -> None:
        source = self.sources[item["type"]]
        self.sender.send(
            source=source,
            destination=self.destination,
            subject=self.get_subject(item),
            message=self.get_message(item),
        )

    def get_default_source(self):
        return self.sources[next(iter(self.sources))]

    @staticmethod
    def get_subject(item: Item) -> str:
        return item["title"]

    @staticmethod
    def get_message(item: Item) -> str:
        message = f"{item['link']}"
        if item["content"]:
            message += f"\n\n{item['content']}"
        return message
