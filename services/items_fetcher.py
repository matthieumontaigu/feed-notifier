import re
import time

from schema.item import Item
from utils.url_utils import extract_netloc
from web_scraper.web_scraper_factory import get_web_scraper


class MultipleItemsFetcher(object):

    def __init__(self, feeds_config):
        self.items_fetchers = [
            ItemsFetcher(**feed_config) for feed_config in feeds_config
        ]

    def fetch(self) -> list[Item]:
        items = []
        for items_fetcher in self.items_fetchers:
            items += items_fetcher.fetch()
        return items


class ItemsFetcher(object):

    def __init__(
        self,
        feed_type: str,
        feed_url: str,
        items_type: str,
        update_interval: int,
        filters: list[str],
    ) -> None:
        self.items_type = items_type
        self.update_interval = update_interval
        self.filters = filters

        self.web_scraper = get_web_scraper(feed_type, feed_url)
        self.last_update_time = 0
        self.domain = extract_netloc(feed_url)

    def fetch(self) -> list[Item]:
        now = time.time()
        if now - self.last_update_time < self.update_interval:
            return []

        items = self.web_scraper.get()
        filtered_items = self.filter(items)
        self.format(filtered_items)
        self.last_update_time = now
        return filtered_items

    def filter(self, items: list[Item]) -> list[Item]:
        if not self.filters:
            return items

        filtered_items = []
        for item in items:
            for pattern in self.filters:
                if re.search(pattern, item["title"]):
                    filtered_items.append(item)
        return filtered_items

    def format(self, items: list[Item]) -> None:
        for item in items:
            item["type"] = self.items_type
            item["domain"] = self.domain
