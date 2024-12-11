import time
import traceback

from services.items_fetcher import MultipleItemsFetcher
from services.memory_manager import MemoryManager
from services.message_sender import MessageSender


class NotifierService(object):

    def __init__(
        self,
        feeds_config: dict,
        message_sender_config: dict,
        memory_manager_config: dict[str, str],
        execution_interval: int,
    ) -> None:
        self.feeds_config = feeds_config
        self.message_sender_config = message_sender_config
        self.memory_manager_config = memory_manager_config
        self.execution_interval = execution_interval

        self.items_fetcher = MultipleItemsFetcher(feeds_config)
        self.memory_manager = MemoryManager(**memory_manager_config)
        self.message_sender = MessageSender(**message_sender_config)

    def start(self) -> None:
        self.send_start_message()
        try:
            while True:
                self.notify()
                self.sleep()
        except Exception as e:
            trace = traceback.format_exc()
            self.send_error_message(trace)

    def notify(self) -> None:
        """
        No notifications are sent when the memory is empty.
        This is because it could lead to a considerable amount of messages sent when fetching for the first time.
        """
        not_notify = self.memory_manager.is_empty()

        items = self.items_fetcher.fetch()
        new_items = self.memory_manager.update(items)
        if not_notify:
            return

        self.message_sender.send_items(new_items)

    def sleep(self) -> None:
        time.sleep(self.execution_interval)

    def send_start_message(self):
        subject = "✅ Feed notifier successfully started"
        message = (
            "You will soon begin receiving notifications from your favorite websites."
        )
        self.message_sender.send_message(subject, message)

    def send_error_message(self, trace: str) -> None:
        subject = "❌ ERROR on feed notifier"
        self.message_sender.send_message(subject, trace)
