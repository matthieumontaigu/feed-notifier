import time
from pathlib import Path

import pandas as pd
from schema.item import Item


class MemoryManager(object):

    def __init__(self, path: str, save_interval: int) -> None:
        self.path = path
        self.save_interval = save_interval

        self.separator = "|"
        self.last_save_time = 0
        self.memory = self.load()

    def load(self):
        if Path(self.path).exists():
            memory = pd.read_csv(self.path, sep=self.separator)
        else:
            memory = pd.DataFrame(
                [], columns=["type", "domain", "title", "date", "link"]
            )

        self.set_index(memory)
        return memory

    def save(self):
        now = time.time()
        if now - self.last_save_time < self.save_interval:
            return

        self.memory.to_csv(self.path, sep=self.separator, index=False)
        self.last_save_time = now

    def update(self, items: list[Item]) -> list[Item]:
        new_items = self.get_new(items)
        self.add(new_items)
        self.save()
        return new_items

    def get_new(self, items: list[Item]) -> list[Item]:
        new_items = []
        for item in items:
            item_index = item["domain"] + item["title"]
            if item_index in self.memory.index:
                continue
            new_items.append(item)
        return new_items

    def add(self, new_items: list[Item]) -> None:
        if not new_items:
            return

        new_items_df = pd.DataFrame(
            [
                {
                    "type": item["type"],
                    "domain": item["domain"],
                    "title": item["title"],
                    "date": item["date"],
                    "link": item["link"],
                }
                for item in new_items
            ]
        )
        self.set_index(new_items_df)
        self.memory = pd.concat([new_items_df, self.memory])

    @staticmethod
    def set_index(df):
        df.index = df["domain"] + df["title"]

    def is_empty(self):
        return len(self.memory) == 0
