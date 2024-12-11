from aws.sender_factory import get_sender


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

    def send_items(self, items: list[dict[str, str]]) -> None:
        for item in items:
            self.send_item(item)

    def send_item(self, item: dict[str, str]) -> None:
        source = self.sources[item["type"]]
        self.sender.send(
            source=source,
            destination=self.destination,
            subject=self.get_subject(item),
            message=self.get_message(item),
        )

    @staticmethod
    def get_subject(item):
        return item["subject"]

    @staticmethod
    def get_message(item):
        return item["message"]
